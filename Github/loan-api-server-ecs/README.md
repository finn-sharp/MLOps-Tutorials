# loan-api-server

`loan-api-server` 폴더는 대출 API 서버 예제 및 실습을 위한 프로젝트입니다.

## 구성

- `README.md`: 프로젝트 개요와 사용 방법
- `.gitignore`: Git에서 제외할 파일 목록
- `requirements.txt`: Python 패키지 의존성 목록

## 설치

```bash
cd Github/loan-api-server
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

## 실행

```bash
uvicorn main:app --reload
```

`main.py` 파일이 없거나 엔트리 포인트가 다르면 실제 파일명과 모듈명을 확인 후 수정하세요.

## 추가 안내

- `.venv` 또는 `env` 폴더는 `.gitignore`에 포함되어 추적되지 않습니다.
- 실제 프로젝트 구조에 맞게 README 내용을 수정하세요.