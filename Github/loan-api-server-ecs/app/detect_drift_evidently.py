"""
데이터 드리프트 감지 

원리: 학습 데이터와 운영 데이터의 평균/비율을 비교해서
      차이가 크면 "드리프트 발생"으로 판단합니다.
"""

import os
import pandas as pd

# 주석된 것은 구버전이고, 에러가 발생하니 새 버전으로 사용하세요
# from evidently.report import Report
# from evidently.metric_preset import DataDriftPreset
from evidently import Report
from evidently.presets import DataDriftPreset

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
DATA_DIR = os.path.join(BASE_DIR, "data")
print("BASE_DIR:", BASE_DIR)
print("DATA_DIR:", DATA_DIR)
    
# 데이터 로드
train_df = pd.read_csv(os.path.join(DATA_DIR, "loan_data.csv"))
pred_df  = pd.read_csv(os.path.join(DATA_DIR, "prediction_logs.csv"))

feature_cols = ["나이", "연소득", "근속연수", "신용점수",
                "기존대출건수", "연간카드사용액", "부채비율",
                "대출신청액", "대출기간",
                "성별", "주거형태", "대출목적", "상환방식"]

ref = train_df[feature_cols]   # Reference (학습)
cur = pred_df[feature_cols]    # Current (운영)

# === 이 3줄이 전부입니다! ===

# 1. Report 객체 생성 — "어떤 분석을 할지" 지정
report = Report(metrics=[DataDriftPreset()])

# 2. 분석 실행 — Reference와 Current를 비교
#    Snapshot 객체가 반환됨
snapshot = report.run(reference_data=ref, current_data=cur)

# 3. HTML 리포트 저장
snapshot.save_html("drift_report.html")