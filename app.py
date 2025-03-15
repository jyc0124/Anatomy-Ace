import streamlit as st
import pandas as pd
import os

# 페이지 설정
st.set_page_config(
    page_title="Anatomy Ace", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS 스타일
st.markdown("""
<style>
    .main-title {
        font-size: 50px !important;
        font-weight: bold;
        color: #1E88E5;
        margin-bottom: 30px;
        text-align: center;
    }
    .subtitle {
        font-size: 24px !important;
        color: #555;
        margin-bottom: 30px;
        text-align: center;
    }
    .section-title {
        font-size: 32px !important;
        font-weight: bold;
        color: #333;
        margin: 30px 0 20px 0;
        border-bottom: 2px solid #1E88E5;
        padding-bottom: 10px;
    }
    .info-text {
        font-size: 20px !important;
        margin-bottom: 10px;
    }
    .success-box {
        background-color: #e8f5e9;
        border-left: 5px solid #4CAF50;
        padding: 15px;
        border-radius: 5px;
        font-size: 20px !important;
        margin: 20px 0;
    }
    .instruction-box {
        background-color: #f5f5f5;
        padding: 20px;
        border-radius: 10px;
        margin: 20px 0;
    }
    .instruction-item {
        font-size: 18px !important;
        margin: 10px 0;
    }
    .stButton button {
        font-size: 22px !important;
        font-weight: bold;
        padding: 12px 30px;
    }
    .stats-card {
        background-color: #e3f2fd;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        margin: 10px 0;
    }
    .stats-number {
        font-size: 28px !important;
        font-weight: bold;
        color: #1E88E5;
    }
    .stats-label {
        font-size: 18px !important;
        color: #555;
    }
</style>
""", unsafe_allow_html=True)

# 메인 페이지 디자인
st.markdown("<div class='main-title'>🧠 Anatomy Ace - 해부학 모의고사</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>해부학 시험 준비를 위한 모의고사 앱입니다.</div>", unsafe_allow_html=True)

# 데이터 로드 - 간단하게 직접 로드
try:
    questions = pd.read_csv("data/questions.csv")
    total_questions = len(questions)
    
    # 문제 수 표시 부분 삭제 (문제가 있으므로 표시하지 않음)
    # st.markdown(f"<div class='success-box'>✅ 총 {total_questions}개의 문제가 로드되었습니다.</div>", unsafe_allow_html=True)
except Exception as e:
    st.error(f"문제 데이터를 로드하는 중 오류가 발생했습니다: {e}")
    st.stop()

# 모의고사 시작 버튼 - 단순화
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("🚀 모의고사 시작하기", type="primary", use_container_width=True):
        # 세션 상태 초기화
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        
        # 단순히 페이지 이동 (URL 파라미터 없이)
        st.switch_page("pages/exam.py")

# 앱 설명
st.markdown("<div class='section-title'>📋 앱 사용 방법</div>", unsafe_allow_html=True)

# 사용 방법 설명
st.markdown("""
<div class='instruction-box'>
    <div class='instruction-item'>1️⃣ '모의고사 시작하기' 버튼을 클릭합니다.</div>
    <div class='instruction-item'>2️⃣ 문제가 나타나면 제한 시간 내에 답변을 입력합니다.</div>
    <div class='instruction-item'>3️⃣ '답변 제출' 버튼을 클릭하거나 시간이 초과되면 자동으로 채점됩니다.</div>
    <div class='instruction-item'>4️⃣ 정답과 내 답변을 비교한 후 '다음 문제로' 버튼을 클릭합니다.</div>
    <div class='instruction-item'>5️⃣ 모든 문제를 풀면 결과를 확인할 수 있습니다.</div>
</div>
""", unsafe_allow_html=True)

# 문제 유형 통계
st.markdown("<div class='section-title'>📊 문제 유형 통계</div>", unsafe_allow_html=True)

type_counts = questions['Type'].value_counts()
단답형_count = type_counts.get('단답형', 0)
서술형_count = type_counts.get('서술형', 0)

col1, col2 = st.columns(2)

with col1:
    st.markdown(f"""
    <div class='stats-card'>
        <div class='stats-number'>{단답형_count}</div>
        <div class='stats-label'>단답형 문제</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class='stats-card'>
        <div class='stats-number'>{서술형_count}</div>
        <div class='stats-label'>서술형 문제</div>
    </div>
    """, unsafe_allow_html=True)

# 연도별 문제 수 (선택 사항)
if 'Year' in questions.columns:
    st.markdown("<div class='section-title'>📅 연도별 문제 통계</div>", unsafe_allow_html=True)
    year_counts = questions['Year'].value_counts().sort_index()
    
    # 연도별 문제 수 표시
    cols = st.columns(len(year_counts))
    for i, (year, count) in enumerate(year_counts.items()):
        with cols[i]:
            st.markdown(f"""
            <div class='stats-card'>
                <div class='stats-number'>{count}</div>
                <div class='stats-label'>{year}년 문제</div>
            </div>
            """, unsafe_allow_html=True)
