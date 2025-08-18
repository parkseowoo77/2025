import streamlit as st
import random

st.set_page_config(page_title="헬로키티 미니 게임", layout="centered")

st.title("🎀 캐릭터 클릭 게임 🎀")
st.write("각 캐릭터의 버튼을 클릭해서 점수를 모아보세요!")

# 세션 스테이트 초기화
if 'kitty_score' not in st.session_state:
    st.session_state.kitty_score = 0
if 'mymelody_score' not in st.session_state:
    st.session_state.mymelody_score = 0
if 'kuromi_score' not in st.session_state:
    st.session_state.kuromi_score = 0

st.markdown("---")

# 헬로키티 섹션
st.subheader("😺 헬로키티")
st.markdown('<div style="background-color:#ffe4e1; padding:10px; border-radius:10px;">🎀 귀여운 핑크 리본!</div>', unsafe_allow_html=True)
if st.button("헬로키티 클릭!"):
    gained = random.randint(1,5)
    st.session_state.kitty_score += gained
    st.success(f"헬로키티가 {gained}점 주었어요! 🎉")
st.write(f"현재 점수: {st.session_state.kitty_score}")

st.markdown("---")

# 마이멜로디 섹션
st.subheader("🐰 마이멜로디")
st.markdown('<div style="background-color:#fff0f5; padding:10px; border-radius:10px;">💖 사랑스러운 리본!</div>', unsafe_allow_html=True)
if st.button("마이멜로디 클릭!"):
    gained = random.randint(2,6)
    st.session_state.mymelody_score += gained
    st.success(f"마이멜로디가 {gained}점 주었어요! 🎉")
st.write(f"현재 점수: {st.session_state.mymelody_score}")

st.markdown("---")

# 쿠로미 섹션
st.subheader("😈 쿠로미")
st.markdown('<div style="background-color:#e6e6fa; padding:10px; border-radius:10px;">🖤 개성있는 검은 리본!</div>', unsafe_allow_html=True)
if st.button("쿠로미 클릭!"):
    gained = random.randint(1,7)
    st.session_state.kuromi_score += gained
    st.success(f"쿠로미가 {gained}점 주었어요! 🎉")
st.write(f"현재 점수: {st.session_state.kuromi_score}")

st.markdown("---")

# 게임 초기화
if st.button("게임 초기화"):
    st.session_state.kitty_score = 0
    st.session_state.mymelody_score = 0
    st.session_state.kuromi_score = 0
    st.info("모든 점수가 초기화되었어요! 🐾")
