import streamlit as st

st.title("진로연계발표 신청자명단")

#객관식 문제 만들기
option = st.radio("수강반 선택", ["A", "B", "C", "D", "E"])
option = st.selectbox("발표하고 싶은 순서", ["1","2","3","4","5"])

agree = st.checkbox("영상 촬영에 동의하시나요?")
if agree:
    st.write("동의하셨군요!")
else:
    st.warning("얼렁 누르세요^^")

#서답형
st.text_input("이름을 입력해주세요.")
#입력값에 따라 문구를 띄우고 싶을 때
topic = st.text_input("주제를 입력해주세요.")
if topic:
    st.error(f"{topic} 잘 준비해 오세요^^")

