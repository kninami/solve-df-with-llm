#!/usr/bin/env python3
"""
semantic_link.py — LLM-Wiki 항목과 SOLVE-IT 항목의 임베딩 기반 semantic linking

wiki/{techniques,weaknesses,mitigations}/*.md (YAML front matter) 와
SOLVE-IT 클론의 data/{techniques,weaknesses,mitigations}/*.json 을
sentence-transformers 임베딩으로 대조하여 항목별 최근접 후보를 찾는다.

설치:
  pip install sentence-transformers pandas openpyxl pyyaml

사용:
  python semantic_link.py --solve-it /path/to/solve-it
  # 모델 변경(기본 all-mpnet-base-v2, 더 빠른 대안: all-MiniLM-L6-v2):
  python semantic_link.py --solve-it ../solve-it --model all-MiniLM-L6-v2

출력: semantic_diff.xlsx
  - summary        타입별 유사도 구간 분포
  - items          위키 항목별 top-3 SOLVE-IT 매칭 + 유사도
  - calibration    유사도 구간별 층화 샘플 (수동 라벨링용: match/partial/no)
"""

import argparse
import json
import random
import re
from pathlib import Path

import pandas as pd
import yaml

WIKI = Path(__file__).parent / "wiki"
TYPES = ["techniques", "weaknesses", "mitigations"]
BANDS = [(0.8, 1.01), (0.7, 0.8), (0.6, 0.7), (0.5, 0.6),
         (0.4, 0.5), (0.3, 0.4), (0.0, 0.3)]
CALIB_PER_BAND = 8  # 구간별 라벨링 샘플 수


def load_wiki(sub):
    items = []
    for f in sorted((WIKI / sub).glob("*.md")):
        text = f.read_text(encoding="utf-8", errors="replace")
        m = re.match(r"^---\n(.*?)\n---", text, re.S)
        if not m:
            continue
        try:
            fm = yaml.safe_load(m.group(1))
        except yaml.YAMLError:
            continue
        if not isinstance(fm, dict):
            continue
        items.append({"id": fm.get("id", ""),
                      "name": str(fm.get("name", f.stem)),
                      "desc": str(fm.get("description", ""))})
    return items


def load_sit(root, sub):
    items = []
    for f in sorted((root / "data" / sub).glob("*.json")):
        d = json.loads(f.read_text(encoding="utf-8"))
        items.append({"id": d.get("id", ""), "name": str(d.get("name", "")),
                      "desc": (str(d.get("description", "")) + " "
                               + str(d.get("details", ""))).strip()})
    return items


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--solve-it", required=True,
                    help="SOLVE-IT 저장소 클론 경로")
    ap.add_argument("--model", default="all-mpnet-base-v2")
    ap.add_argument("--out", default="semantic_diff.xlsx")
    args = ap.parse_args()

    from sentence_transformers import SentenceTransformer, util
    print(f"모델 로딩: {args.model}")
    model = SentenceTransformer(args.model)
    sit_root = Path(args.solve_it)

    all_rows, summary = [], []
    for t in TYPES:
        wiki, sit = load_wiki(t), load_sit(sit_root, t)
        print(f"{t}: wiki {len(wiki)} vs solve-it {len(sit)} 인코딩 중...")
        wtexts = [f"{w['name']}. {w['desc']}" for w in wiki]
        stexts = [f"{s['name']}. {s['desc']}" for s in sit]
        we = model.encode(wtexts, convert_to_tensor=True,
                          show_progress_bar=True, normalize_embeddings=True)
        se = model.encode(stexts, convert_to_tensor=True,
                          show_progress_bar=True, normalize_embeddings=True)
        sim = util.cos_sim(we, se).cpu().numpy()

        band_counts = {f"{lo:.1f}–{hi if hi <= 1 else 1.0:.1f}": 0
                       for lo, hi in BANDS}
        for i, w in enumerate(wiki):
            order = sim[i].argsort()[::-1][:3]
            best = float(sim[i][order[0]])
            for lo, hi in BANDS:
                if lo <= best < hi:
                    band_counts[f"{lo:.1f}–{hi if hi <= 1 else 1.0:.1f}"] += 1
                    break
            row = {"type": t, "wiki_id": w["id"], "wiki_name": w["name"],
                   "best_sim": round(best, 3)}
            for rank, j in enumerate(order, 1):
                row[f"match{rank}_id"] = sit[j]["id"]
                row[f"match{rank}_name"] = sit[j]["name"]
                row[f"match{rank}_sim"] = round(float(sim[i][j]), 3)
            all_rows.append(row)
        summary.append({"type": t, "wiki_n": len(wiki),
                        "solveit_n": len(sit), **band_counts})

    items = pd.DataFrame(all_rows).sort_values(
        ["type", "best_sim"], ascending=[True, False])

    # 층화 캘리브레이션 샘플: 구간별 무작위 N쌍 → 수동 라벨링
    random.seed(42)
    calib = []
    for t in TYPES:
        sub = items[items["type"] == t]
        for lo, hi in BANDS:
            band = sub[(sub["best_sim"] >= lo) & (sub["best_sim"] < hi)]
            take = band.sample(min(CALIB_PER_BAND, len(band)),
                               random_state=42)
            for _, r in take.iterrows():
                calib.append({
                    "type": t, "band": f"{lo:.1f}–{min(hi,1.0):.1f}",
                    "wiki_id": r["wiki_id"], "wiki_name": r["wiki_name"],
                    "match_id": r["match1_id"],
                    "match_name": r["match1_name"],
                    "sim": r["best_sim"],
                    "label": "",   # match / partial / no  ← 수동 기입
                    "notes": "",
                })
    calib_df = pd.DataFrame(calib)

    with pd.ExcelWriter(args.out, engine="openpyxl") as w:
        pd.DataFrame(summary).to_excel(w, index=False, sheet_name="summary")
        items.to_excel(w, index=False, sheet_name="items")
        calib_df.to_excel(w, index=False, sheet_name="calibration")
        for name in ("items", "calibration"):
            ws = w.sheets[name]
            ws.freeze_panes = "A2"
            ws.auto_filter.ref = ws.dimensions
    print(f"\n저장: {args.out}")
    print(pd.DataFrame(summary).to_string(index=False))
    print(f"\ncalibration 시트 {len(calib_df)}쌍의 label 컬럼을 "
          f"match/partial/no 로 채우면 threshold를 정할 수 있습니다.")


if __name__ == "__main__":
    main()
