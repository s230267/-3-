# 분류 모델 웹앱 만들기
import streamlit as st

# 1. 기계학습 모델 파일 로드
import joblib
model=joblib.load('logistic_regression_model.pkl')

# 2. 모델 설명
st.title('폭염 예측 에이전트')
st.subheader('모델 설명 ')
st.write(' - 기계학습 알고리즘 : 로지스틱 회귀 ')
st.write(' - 학습 데이터 출처 : https://data.kma.go.kr/data/weatherIssue/slthtList.do?pgmNo=690')
st.write(' - 훈련    데이터 : 3321건')
st.write(' - 테스트 데이터 : 1424건')
st.write(' - 모델 정확도 :0.97 ')
st.subheader('데이터시각화1')
st.image('시각화1.png')
st.subheader('데이터시각화2')
st.image('시각화2.png')
st.subheader('데이터시각화3')
st.image('시각화3.png')
st.subheader('데이터시각화4')
st.image('시각화4.png')
st.subheader('데이터시각화5')
st.image('시각화5.png')


# 4. 모델 활용
st.subheader('모델 활용')
st.write('--다음 수치들을 입력하세요.인공지능이 폭염 여부를 판단해드립니다.--')
st.write('--입력된 수치들은 결괏값 예측 이외의 목적으로 사용되어지지 않습니다.--')

a=st.number_input('최고 기온 입력',value=0)
b=st.number_input('최저 기온 입력',value=0)
c=st.number_input('평균 상대 습도 입력',value=0)
d=st.selectbox('자외선 지수 선택(낮음:0,보통:1,높음:2,매우 높음:3,위험:4',[0,1,2,3,4])

if st.button('폭염 예측'):
  input_data=[[a,b,c,d]]
  p=model.predict(input_data)
  if p[0]==0:
       st.success('예측 결과는 폭염이 아닙니다.')
  else:
       st.success('예측 결과는 폭염입니다.')
