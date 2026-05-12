# KDI 정책자료 아카이브 (kdi-policy-archive)

KDI 경제정보센터의 정책자료 RSS를 주기적으로 수집하고, 산업 키워드에 따라 자동 분류하여 누적 저장하는 아카이브 사이트입니다.

## 기능
- **자동 수집**: 매시간 KDI RSS 피드를 확인하여 신규 자료 추가 (GitHub Actions)
- **자동 분류**: 사용자가 정의한 키워드(`categories.json`)를 바탕으로 카테고리 자동 태깅
- **검색 및 필터**: 카테고리 다중 필터, 텍스트 검색, 기간 필터 지원
- **통계 제공**: 카테고리별 누적 개수 및 월별 추이 차트 시각화
- **무료 운영**: 데이터베이스 없이 JSON 파일과 GitHub Pages 만으로 운영

## 파일 구조
- `.github/workflows/`: 자동 수집 및 재분류를 위한 GitHub Actions 워크플로우
- `scripts/`: Python 기반 RSS 수집기 및 키워드 분류기
- `docs/`: GitHub Pages로 배포되는 프론트엔드 웹사이트 루트
  - `docs/data/archive.json`: 누적된 정책자료 데이터
  - `docs/data/categories.json`: 분류 카테고리 및 키워드 설정

## 카테고리 추가/수정 방법
새로운 산업 분야를 모니터링하거나 기존 키워드를 수정하려면 `docs/data/categories.json` 파일만 수정하면 됩니다.

1. GitHub 리포지토리에서 `docs/data/categories.json` 파일 열기
2. 파일 수정
3. `categories` 배열에 새로운 항목을 추가하거나 기존 `keywords` 목록 수정
4. 커밋을 저장하면 GitHub Actions(`reclassify.yml`)가 자동으로 실행되어 **기존 모든 데이터의 카테고리를 재분류**합니다.

```json
{
  "id": "new_category",
  "label": "새분야",
  "color": "#FF5733",
  "keywords": ["키워드1", "키워드2"]
}
```

## 로컬 실행 방법 (프론트엔드)
별도의 서버 없이 `docs/index.html` 파일을 브라우저에서 직접 열거나, VSCode Live Server 등으로 실행하면 확인 가능합니다.

## 개발 스택
- **Backend**: Python 3, feedparser, BeautifulSoup4
- **Frontend**: HTML5, Vanilla JavaScript, Tailwind CSS (CDN), Chart.js
- **CI/CD & Hosting**: GitHub Actions, GitHub Pages
