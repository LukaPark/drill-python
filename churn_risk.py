# 예시: 로지스틱 회귀 모델을 사용한 이탈 확률 예측
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np
import pandas as pd

# 데이터 로드 및 전처리
# df = pd.read_csv('your_data.csv')
# X = df.drop('is_churned', axis=1)  # 이탈 여부를 제외한 특성
# y = df['is_churned']  # 이탈 여부

# 데이터 분할
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 모델 학습
model = LogisticRegression()
model.fit(X_train, y_train)

# 예측 및 평가
predictions = model.predict_proba(X_test)[:, 1]  # 이탈할 확률
