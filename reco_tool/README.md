# SOLVE-IT Extension — 콘텐츠 추천 도구

LLM-Wiki(디지털 포렌식 논문 493편에서 추출한 지식베이스)를 관심 키워드로 검색해,
SOLVE-IT에 추가할 후보를 **보강(augment)** / **신규(new)** 로 나눠 추천하는 도구.
각 추천은 참고문헌·DOI·피인용수·적합도 점수를 근거로 제시하며, 선택 시 SOLVE-IT의
GitHub 이슈 폼으로 프리필된다.

## 바로 쓰기

- **웹(권장)**: GitHub Pages URL 접속 → 키워드 입력 → 추천 확인
- **로컬**: `index.html`을 브라우저로 열기 (더블클릭 가능). 데이터가
  `reco_data.js`에 인라인되어 있어 서버 없이 동작한다.

토큰·API 키·로그인 불필요. 키워드 검색은 브라우저 안에서 텍스트 매칭으로 동작한다.

## 파일

| 파일 | 역할 |
|---|---|
| `index.html` | 도구 본체 (검색·추천·이슈 프리필) |
| `reco_data.js` | 위키+링킹+인용 데이터 번들 (index.html이 읽음) |
| `build_data.py` | 위키·semantic_diff·인용캐시 → 데이터 번들 생성 |
| `fetch_citations.py` | OpenAlex로 DOI별 피인용수 조회 → 캐시 |

## 데이터 갱신 (관리자용)

```bash
# 1) (선택) 피인용수 캐시 갱신 — 순위에 반영됨
python fetch_citations.py --email you@example.com

# 2) 데이터 번들 재생성
python build_data.py            # → reco_data.json + reco_data.js

# 3) 커밋·푸시하면 GitHub Pages에 자동 반영
git add reco_tool/ && git commit -m "Update reco data" && git push
```

보강/신규 분류 경계(threshold)는 `build_data.py --t-techniques 0.65` 등으로 조정.

## GitHub Pages 배포

저장소 Settings → Pages → Source를 `main` 브랜치 `/ (root)` 로 지정하면
`https://<user>.github.io/<repo>/reco_tool/` 에서 도구가 열린다.
(저장소가 public 이어야 무료 Pages 사용 가능)
