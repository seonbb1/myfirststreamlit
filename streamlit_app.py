import streamlit as st

st.title("👋🏻 연수 실습 페이지(1023)")
st.subheader("문현고 과학정보부")
st.write("생명과학 1 담당")

# st.write("링크") 이렇게 하면 연결은 되는데 안예쁨...밑에처럼 하면 버튼이 생김
st.link_button("깃허브 프로필 클릭!", "https://github.com/seonbb1")

#강조해서 글 쓰고 싶을 때
st.success("초록색 창")
st.error("빨간색 창")
st.info("파란색 창")
st.warning("노란색 창") # ctrl+/ : 한번에 주석처리할때 단축

#이미지 넣기, 캡션 넣기
st.image("https://media.giphy.com/media/Eq49yQGJL835K/giphy.gif?cid=790b7611jfoucyqytiavw61vmtx6s36uw3o2twpv05eqsbdf&ep=v1_gifs_search&rid=giphy.gif&ct=g", caption="가장 좋아하는 동물은 펭귄") 
st.video("https://www.youtube.com/watch?v=vp0ZsOrj6o0")
st.write("귀여운 쇠족제비 영상 보고 가세요")

#저장은 소스제어 -> 
