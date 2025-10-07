# Whoogle Search MCP

Open WebUI 통합을 위해 특별히 설계된 Whoogle 검색 엔진과 연동하는 FastAPI 기반 검색 프록시 서버입니다.

## 개요

이 프로젝트는 Open WebUI 및 기타 AI 채팅 애플리케이션에서 검색 기능이 필요한 경우를 위해 설계된 Whoogle 검색 엔진의 REST API 래퍼입니다. 검색 결과를 일관된 형식으로 정규화하고 Open WebUI의 검색 기능과 원활하게 통합되는 깔끔한 API 인터페이스를 제공합니다.

### Open WebUI 통합

이 서비스는 Open WebUI를 위한 **검색 프록시** 역할을 하며, 사용자가 다음을 가능하게 합니다:
- Whoogle(프라이버시 중심의 Google 검색 대안)을 통한 웹 검색 수행
- AI 대화에서 실시간 검색 결과 받기
- 웹 정보에 접근하면서 프라이버시 유지
- Google에 개인 데이터를 노출하지 않고 검색 기능 사용

## 주요 기능

- 🔍 **Open WebUI 통합**: Open WebUI에서 검색 도구로 원활하게 통합
- 🚀 **FastAPI 백엔드**: 고성능 비동기 웹 프레임워크
- 📊 **정규화된 결과**: AI 채팅 인터페이스와 호환되는 일관된 JSON 응답 형식
- 🔒 **프라이버시 중심**: Whoogle(프라이버시 중심의 Google 검색 대안) 사용
- 🐳 **Docker 지원**: Docker 및 Docker Compose를 통한 쉬운 배포
- ⚙️ **설정 가능**: 유연한 배포를 위한 환경 기반 구성
- 🌐 **실시간 검색**: AI 대화에서 라이브 웹 검색 결과 제공

## API 엔드포인트

### GET /search

Whoogle을 통해 검색 쿼리를 수행하고 정규화된 결과를 반환합니다.

**매개변수:**
- `q` 또는 `query`: 검색 쿼리 문자열 (필수)

**응답 형식:**
```json
{
  "query": "검색어",
  "number_of_results": 10,
  "results": [
    {
      "url": "https://example.com",
      "title": "예시 제목",
      "content": "예시 설명",
      "img_src": "https://example.com/image.jpg",
      "engine": "whoogle",
      "category": "general"
    }
  ],
  "answers": [],
  "infoboxes": []
}
```

## 설치

### 사전 빌드된 Docker 이미지 사용 (권장)

최신 Docker 이미지는 모든 릴리스에서 자동으로 빌드되어 Docker Hub에 푸시됩니다:

```bash
docker run -p 8080:8080 -e WHOOGLE_BASE_URL=http://your-whoogle-instance:5000 your-username/whoogle-search-mcp:latest
```

### 소스에서 빌드

1. 저장소 클론:
```bash
git clone https://github.com/your-username/whoogle-search-mcp.git
cd whoogle-search-mcp
```

2. Docker로 빌드 및 실행:
```bash
docker build -t whoogle-search-mcp .
docker run -p 8080:8080 -e WHOOGLE_BASE_URL=http://your-whoogle-instance:5000 whoogle-search-mcp
```

### 로컬 개발

1. 의존성 설치:
```bash
pip install -r requirements.txt
```

2. 환경 변수 설정:
```bash
export WHOOGLE_BASE_URL=http://localhost:5000
```

3. 애플리케이션 실행:
```bash
uvicorn app:app --host 0.0.0.0 --port 8080
```

## Open WebUI 설정

### Open WebUI에서 검색 프록시 설정

1. **이 서비스를 Docker 또는 로컬에서 배포**
2. **Open WebUI를 이 서비스를 검색 프록시로 사용하도록 설정**:
   - Open WebUI 설정으로 이동
   - "도구" 또는 "검색" 섹션으로 이동
   - 다음 구성으로 새로운 검색 도구 추가:
     - **이름**: Whoogle 검색
     - **URL**: `http://your-server:8080/search`
     - **방법**: GET
     - **매개변수**: `q` (쿼리 매개변수)

### 환경 변수

- `WHOOGLE_BASE_URL`: Whoogle 인스턴스의 URL (기본값: `http://whoogle:5000`)

### 설정 파일

`env.sample`을 `.env`로 복사하고 필요에 따라 값을 수정하세요:

```bash
cp env.sample .env
```

`env.sample` 파일의 내용:
```bash
# Whoogle Search MCP Server Configuration

# Whoogle server url
# 기본값: http://whoogle:5000
WHOOGLE_BASE_URL=http://whoogle:5000

# 예시:
# WHOOGLE_BASE_URL=http://localhost:5000
# WHOOGLE_BASE_URL=https://your-whoogle-instance.com
```

### 설정 예시

```bash
# 로컬 개발용
WHOOGLE_BASE_URL=http://localhost:5000

# 프로덕션용
WHOOGLE_BASE_URL=https://your-whoogle-instance.com
```

### Docker Compose 예시 (Open WebUI와 함께)

```yaml
version: '3.8'
services:
  whoogle-search-mcp:
    image: your-username/whoogle-search-mcp:latest
    ports:
      - "8080:8080"
    environment:
      - WHOOGLE_BASE_URL=http://whoogle:5000
    depends_on:
      - whoogle

  whoogle:
    image: benbusby/whoogle-search:latest
    ports:
      - "5000:5000"

  open-webui:
    image: ghcr.io/open-webui/open-webui:main
    ports:
      - "3000:8080"
    environment:
      - OPENAI_API_BASE_URL=http://your-llm-server:8000/v1
```

## 사용 예시

### 기본 검색
```bash
curl "http://localhost:8080/search?q=파이썬 프로그래밍"
```

### 쿼리 매개변수 사용
```bash
curl "http://localhost:8080/search?query=머신러닝"
```

## 개발

### 프로젝트 구조
```
whoogle-search-mcp/
├── app.py                    # 메인 FastAPI 애플리케이션
├── requirements.txt          # Python 의존성
├── Dockerfile               # Docker 구성
├── env.sample               # 환경 변수 템플릿
├── README.md                # 영어 문서
├── README.ko.md             # 한국어 문서
├── LICENSE                  # MIT 라이선스
└── .github/
    └── workflows/
        └── docker-build.yml # Docker Hub용 GitHub Actions
```

### 의존성
- **FastAPI**: API 구축을 위한 웹 프레임워크
- **httpx**: Whoogle에 요청을 보내기 위한 비동기 HTTP 클라이언트
- **uvicorn**: 애플리케이션 실행을 위한 ASGI 서버

### CI/CD 파이프라인
- **GitHub Actions**: Docker Hub로의 자동 Docker 이미지 빌드 및 푸시
- **멀티 플랫폼 지원**: linux/amd64 및 linux/arm64 아키텍처용 빌드
- **자동 태깅**: 브랜치, 버전 및 최신 릴리스용 태그 생성

## 라이선스

이 프로젝트는 MIT 라이선스 하에 있습니다. 자세한 내용은 [LICENSE](LICENSE) 파일을 참조하세요.

## 기여하기

1. 저장소 포크
2. 기능 브랜치 생성
3. 변경사항 적용
4. 풀 리퀘스트 제출

## 요구사항

- Python 3.11+
- 실행 중인 Whoogle 인스턴스에 대한 액세스
- Docker (선택사항, 컨테이너화된 배포용)
