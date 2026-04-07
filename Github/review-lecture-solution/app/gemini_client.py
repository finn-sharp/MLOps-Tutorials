from google import genai
from google.genai import types

import os
from dotenv import load_dotenv
load_dotenv()

GEMINI_API = os.getenv("GEMINI_API")
client = genai.Client(api_key=GEMINI_API)

prompt = """주어진 리뷰 텍스트를 분석해주세요.

리뷰 : 상품 색상이 사진과 너무 달라요.

다음 기준으로 분석하세요 :
- sentiment : '긍정', '부정', '중립' 중 하나
- category : '배송', '품질', '가격', '고객서비스', '기타' 중 하나
- summary : 리뷰 핵심을 1~2문장으로 요약
- confidence : 0.0 ~ 1.0 사이의 신뢰도"""

response = client.models.generate_content(
    model="gemini-2.5-flash-lite",
    contents=prompt,

    # Prompt Engineering의 영역
    config=types.GenerateContentConfig(
        # json으로 응답하도록 설정**
        response_mime_type="application/json",
        response_schema={
            "type" : "object",
            "properties" : {
                "sentiment" : {"type" : "string"},
                "category" : {"type" : "string"},
                "summary" : {"type" : "string"},
                "confidence" : {"type" : "number"}
            },
            "required" : ["sentiment", "category", "summary", "confidence"]
        }
    )
    
)
print(response.text)