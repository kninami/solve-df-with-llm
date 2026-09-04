#!/usr/bin/env python3
"""
build_data.py — 추천 도구용 데이터 번들(reco_data.json) 생성

입력:
  ../wiki/{techniques,weaknesses,mitigations}/*.md   (LLM-Wiki 항목)
  ../references/doi_metadata.csv                       (레퍼런스 메타/DOI)
  semantic_diff.xlsx (items 시트)                      (사전계산 linking)
  citations_cache.json (선택)                          (fetch_citations.py 산출)

출력:
  reco_data.json  — 단일 HTML 도구(index.html)가 읽는 데이터

분류(보강/신규)는 best_sim 과 타입별 threshold 로 판정:
  best_sim >= T[type]  → 보강(augment, 기존 SOLVE-IT 항목에 추가)
  best_sim <  T[type]  → 신규(new)
threshold 는 calibration 기반 잠정값이며 --t-* 로 조정 가능.
"""
import argparse
import csv
import json
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent
WIKI = ROOT.parent / "wiki"
DOI_CSV = ROOT.parent / "references" / "doi_metadata.csv"
TYPES = ["techniques", "weaknesses", "mitigations"]

# 타입별 "보강" 판정 threshold (calibration 잠정값; 근거 순위엔 미사용, 분류에만)
DEFAULT_T = {"techniques": 0.62, "weaknesses": 0.58, "mitigations": 0.56}


def parse_md(path):
    text = path.read_text(encoding="utf-8", errors="replace")
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.S)
    if not m:
        return None
    try:
        fm = yaml.safe_load(m.group(1))
    except yaml.YAMLError:
        return None
    if not isinstance(fm, dict):
        return None
    body = m.group(2)
    sm = re.search(r"## Summary\s*\n(.+?)(?:\n##|\Z)", body, re.S)
    summary = re.sub(r"\s+", " ", sm.group(1)).strip() if sm else ""
    return fm, summary


def load_refs():
    refs = {}
    if not DOI_CSV.exists():
        return refs
    with DOI_CSV.open(encoding="utf-8") as f:
        for row in csv.DictReader(f):
            rid = row.get("reference_id", "")
            if rid:
                refs[rid] = {
                    "title": row.get("title", ""),
                    "authors": row.get("authors", ""),
                    "year": row.get("year", ""),
                    "doi": (row.get("doi") or row.get("doi_url")
                            or row.get("url") or "").strip(),
                }
    return refs


def load_linking(xlsx):
    import pandas as pd
    df = pd.read_excel(xlsx, sheet_name="items")
    out = {}
    for _, r in df.iterrows():
        out[str(r["wiki_id"])] = {
            "best_sim": float(r["best_sim"]),
            "matches": [
                {"id": str(r[f"match{i}_id"]),
                 "name": str(r[f"match{i}_name"]),
                 "sim": float(r[f"match{i}_sim"])}
                for i in (1, 2, 3) if str(r.get(f"match{i}_id", "")) != "nan"
            ],
        }
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--semantic-diff", default="semantic_diff.xlsx")
    ap.add_argument("--citations", default="citations_cache.json")
    ap.add_argument("--out", default="reco_data.json")
    for t in TYPES:
        ap.add_argument(f"--t-{t}", type=float, default=DEFAULT_T[t])
    args = ap.parse_args()

    thr = {t: getattr(args, f"t_{t}") for t in TYPES}
    refs = load_refs()
    linking = load_linking(args.semantic_diff)
    cites = {}
    cpath = ROOT / args.citations
    if cpath.exists():
        cites = json.loads(cpath.read_text(encoding="utf-8"))
        print(f"인용 캐시 로드: {len(cites)} DOI")
    else:
        print("인용 캐시 없음 — fetch_citations.py 를 먼저 실행하면 순위에 반영됨")

    items = []
    for t in TYPES:
        for f in sorted((WIKI / t).glob("*.md")):
            parsed = parse_md(f)
            if not parsed:
                continue
            fm, summary = parsed
            wid = fm.get("id", "")
            link = linking.get(wid, {"best_sim": 0.0, "matches": []})
            src = fm.get("source_refs") or []
            ref_objs, max_cite = [], 0
            for rid in src:
                meta = refs.get(rid, {})
                doi = meta.get("doi", "")
                c = cites.get(doi.lower().replace("https://doi.org/", ""), None)
                if c is not None:
                    max_cite = max(max_cite, c)
                ref_objs.append({"id": rid, **meta, "cited_by": c})
            best = link["best_sim"]
            items.append({
                "id": wid, "type": t, "name": str(fm.get("name", f.stem)),
                "summary": summary,
                "description": str(fm.get("description", "")),
                "objective_ids": fm.get("objective_ids") or [],
                "best_sim": round(best, 3),
                "matches": link["matches"],
                "class": "augment" if best >= thr[t] else "new",
                "refs": ref_objs,
                "max_cited_by": max_cite,
            })
    bundle = {
        "generated_from": "LLM-Wiki + SOLVE-IT semantic diff",
        "thresholds": thr,
        "has_citations": bool(cites),
        "counts": {
            t: {"total": sum(1 for i in items if i["type"] == t),
                "augment": sum(1 for i in items
                               if i["type"] == t and i["class"] == "augment"),
                "new": sum(1 for i in items
                           if i["type"] == t and i["class"] == "new")}
            for t in TYPES},
        "items": items,
    }
    payload = json.dumps(bundle, ensure_ascii=False)
    Path(ROOT / args.out).write_text(payload, encoding="utf-8")
    # file:// 에서 index.html 이 fetch 없이 읽도록 JS 번들도 생성
    Path(ROOT / "reco_data.js").write_text(
        "window.RECO_DATA = " + payload + ";", encoding="utf-8")
    print(f"저장: {args.out} + reco_data.js ({len(items)} 항목)")
    for t in TYPES:
        c = bundle["counts"][t]
        print(f"  {t}: 총 {c['total']} = 보강 {c['augment']} + 신규 {c['new']}")


if __name__ == "__main__":
    main()
