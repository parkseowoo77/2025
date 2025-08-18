import streamlit as st
import random

st.set_page_config(page_title="단어 궁합 앱 🐱🐶", layout="centered")

st.title("🐱🐶 좋아하는 단어 궁합 앱")
st.write("각자 좋아하는 단어를 입력하면 궁합 점수를 확인해보세요!")

# 사용자 입력
word1 = st.text_input("첫 번째 사람의 좋아하는 단어")
word2 = st.text_input("두 번째 사람의 좋아하는 단어")

if st.button("궁합 보기"):
    if word1 and word2:
        # 캐릭터 이모지: 고양이 1 + 강아지 1
        st.markdown(f"🐱 {word1}  💕  {word2} 🐶", unsafe_allow_html=True)

        # 점수 계산: 0~100
        length_score = max(0, 20 - abs(len(word1) - len(word2)))  # 최대 20
        common_letters = len(set(word1) & set(word2)) * 5          # 겹치는 글자 1개당 5점
        random_score = random.randint(0, 60)                      # 랜덤 요소 최대 60
        total_score = length_score + common_letters + random_score
        total_score = min(total_score, 100)                       # 최대 100점

        # 점수별 효과
        if total_score > 80:
            st.balloons()  # 폭죽/풍선
            st.markdown('<h3 style="color:#ff1493">🎉 완전 찰떡 궁합! 🎉</h3>', unsafe_allow_html=True)
            st.write("👏 박수와 함께 축하해요! 너무 잘 맞아요! 😻🐶")
        elif total_score > 50:
            st.markdown('<h3 style="color:#ff69b4">💕 서로 잘 맞는 편이에요! 💕</h3>', unsafe_allow_html=True)
            st.write("🎈 귀여운 하트와 풍선이 터졌어요! 😺🐶")
        else:
            st.markdown('<h3 style="color:#1e90ff">☔ 조금 아쉬운 궁합이에요 ☔</h3>', unsafe_allow_html=True)
            st.write("💧 비가 내리는 분위기지만, 노력하면 좋아질 수 있어요! 😿🐶")
            # 간단 비 애니메이션
            st.markdown(
                """
                <style>
                @keyframes rain {
                    0% {top: -10px;}
                    100% {top: 100%;}
                }
                .drop {
                    position: absolute;
                    width: 2px;
                    height: 10px;
                    background: #1e90ff;
                    animation: rain 1s linear infinite;
                }
                </style>
                <div class="drop"></div>
                <div class="drop" style="left: 30px; animation-delay: 0.3s;"></div>
                <div class="drop" style="left: 60px; animation-delay: 0.6s;"></div>
                """, unsafe_allow_html=True
            )

        st.markdown(f"<p style='font-size:20px'>💌 점수: {total_score}/100</p>", unsafe_allow_html=True)
    else:
        st.warning("두 사람의 단어를 모두 입력해주세요! 📝")
