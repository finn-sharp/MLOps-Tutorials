# ===== 기본적인 Dockerfile 구조 =====

# 1. 가벼운 Python 3.10 이미지를 쓸게요
FROM python:3.10-slim

# 2. 작업 디렉토리를 설정할게요 (기준은 Dockerfile이 있는 위치)
WORKDIR /app

# 3. 필요한 패키지를 docker 이미지에 복사하고 설치할게요 
# 이 작업을 하는 이유는, requirements.txt 파일이 변경되지 않으면 Docker가 캐시를 사용해서 빠르게 빌드할 수 있기 때문이에요
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. 이후 나머지 소스 코드들도 docker 이미지에 모두 복사할게요
COPY . .

# 5. 컨테이너가 통신할 수 있도록 포트를 열어줄게요
EXPOSE 8000

# 6. 컨테이너가 시작될 때 실행할 명령어를 설정할게요
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]