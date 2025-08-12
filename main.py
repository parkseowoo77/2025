import streamlit as st

# MBTI별 추천 직업 데이터
job_data = {
    "INTJ": ["전략 컨설턴트", "데이터 과학자", "엔지니어"],
    "ENFP": ["마케터", "광고 기획자", "작가"],
    "ISTP": ["기계공", "파일럿", "프로게이머"],
    "INFJ": ["심리상담사", "작가", "인권변호사"],
    # ... 나머지 MBTI도 추가
}

st.title("💡 MBTI 기반 진로 추천 앱")
st.write("당신의 MBTI를 입력하면 어울리는 직업을 추천해드려요!")

# MBTI 입력
mbti = st.selectbox(
    "당신의 MBTI를 선택하세요:",
    options=sorted(job_data.keys())
)

if st.button("추천 받기"):
    jobs = job_data.get(mbti, [])
    if jobs:
        st.subheader(f"📌 {mbti} 유형 추천 직업")
        for job in jobs:
            st.write(f"- {job}")
    else:
        st.warning("아직 데이터가 준비되지 않았어요!")

