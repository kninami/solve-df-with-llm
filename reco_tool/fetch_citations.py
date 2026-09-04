#!/usr/bin/env python3
"""
fetch_citations.py — 위키 레퍼런스의 DOI별 피인용수를 OpenAlex에서 조회해 캐시

산출: citations_cache.json  { "<정규화 doi>": cited_by_count, ... }
build_data.py 가 이 캐시를 읽어 추천 순위에 피인용수를 반영한다.

사용:
  python fetch_citations.py --email you@example.com
  # 갱신(기존 캐시 무시하고 다시): --refresh

OpenAlex 배치 API로 DOI 50개씩 조회. 인터넷 되는 로컬에서 실행.
"""
import argparse
import csv
import json
import re
import time
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parent
DOI_CSV = ROOT.parent / "references" / "doi_metadata.csv"
CACHE = ROOT / "citations_cache.json"
OPENALEX = "https://api.openalex.org/works"


def norm_doi(d):
    d = (d or "").strip().lower()
    d = re.sub(r"^https?://(dx\.)?doi\.org/", "", d)
    return d


def collect_dois():
    dois = set()
    with DOI_CSV.open(encoding="utf-8") as f:
        for row in csv.DictReader(f):
            d = norm_doi(row.get("doi") or row.get("doi_url") or "")
            if d.startswith("10."):
                dois.add(d)
    return sorted(dois)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--email", required=True)
    ap.add_argument("--refresh", action="store_true")
    args = ap.parse_args()

    cache = {}
    if CACHE.exists() and not args.refresh:
        cache = json.loads(CACHE.read_text(encoding="utf-8"))
    dois = [d for d in collect_dois() if d not in cache]
    print(f"조회 대상 DOI: {len(dois)} (캐시 보유 {len(cache)})")

    for i in range(0, len(dois), 50):
        batch = dois[i:i + 50]
        flt = "doi:" + "|".join(batch)
        try:
            r = requests.get(OPENALEX, params={
                "filter": flt, "per-page": 50,
                "select": "doi,cited_by_count", "mailto": args.email},
                timeout=60)
            r.raise_for_status()
            found = {}
            for w in r.json().get("results", []):
                d = norm_doi(w.get("doi") or "")
                if d:
                    found[d] = w.get("cited_by_count", 0)
            for d in batch:
                cache[d] = found.get(d, 0)  # 미발견은 0
        except requests.RequestException as e:
            print(f"  배치 실패({i}): {e}")
        CACHE.write_text(json.dumps(cache, ensure_ascii=False),
                         encoding="utf-8")
        print(f"  {min(i + 50, len(dois))}/{len(dois)}")
        time.sleep(1.0)
    print(f"저장: {CACHE} ({len(cache)} DOI)")


if __name__ == "__main__":
    main()
