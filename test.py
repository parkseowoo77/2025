import streamlit as st
import random

st.set_page_config(page_title="메이크업 클릭 게임", layout="centered")

st.title("💄 메이크업 클릭 게임 💄")
st.write("각 메이크업 아이템 버튼을 클릭해서 점수를 모아보세요!")

# 세션 스테이트 초기화
if 'lipstick_score' not in st.session_state:
    st.session_state.lipstick_score = 0
if 'blusher_score' not in st.session_state:
    st.session_state.blusher_score = 0
if 'eyeshadow_score' not in st.session_state:
    st.session_state.eyeshadow_score = 0

st.markdown("---")

# 립스틱 섹션
st.subheader("💋 립스틱")
st.markdown('<div style="background-color:#ffccd5; padding:10px; border-radius:10px;">💖 화사한 핑크 립!</div>', unsafe_allow_html=True)
if st.button("립스틱 클릭!"):
    gained = random.randint(1,5)
    st.session_state.lipstick_score += gained
    st.success(f"립스틱이 {gained}점 주었어요! 🎉")
st.write(f"현재 점수: {st.session_state.lipstick_score}")

st.markdown("---")

# 블러셔 섹션
st.subheader("🌸 블러셔")
st.markdown('<div style="background-color:#ffe4e1; padding:10px; border-radius:10px;">💗 사랑스러운 치크!</div>', unsafe_allow_html=True)
if st.button("블러셔 클릭!"):
    gained = random.randint(2,6)
    st.session_state.blusher_score += gained
    st.success(f"블러셔가 {gained}점 주었어요! 🎉")
st.write(f"현재 점수: {st.session_state.blusher_score}")

st.markdown("---")

# 아이섀도우 섹션
st.subheader("✨ 아이섀도우")
st.markdown('<div style="background-color:#d8bfd8; padding:10px; border-radius:10px;">💜 반짝이는 아이!</div>', unsafe_allow_html=True)
if st.button("아이섀도우 클릭!"):
    gained = random.randint(1,7)
    st.session_state.eyeshadow_score += gained
    st.success(f"아이섀도우가 {gained}점 주었어요! 🎉")
st.write(f"현재 점수: {st.session_state.eyeshadow_score}")

st.markdown("---")

# 게임 초기화
if st.button("게임 초기화"):
    st.session_state.lipstick_score = 0
    st.session_state.blusher_score = 0
    st.session_state.eyeshadow_score = 0
    st.info("모든 점수가 초기화되었어요! 💖")
