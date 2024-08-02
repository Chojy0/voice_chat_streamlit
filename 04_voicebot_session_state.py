# streamlit 패키지 추가
import streamlit as st

# OpenAI 패키지 추가
import openai
import os
from dotenv import load_dotenv

# .env 파일 경로 지정, .env 파일이 현재 directory가 아닐 때 위치 변경해야 함. 
load_dotenv()


# OpenAI API 키 설정하기
api_key = os.environ.get('open_api_key')

client = openai.OpenAI(api_key=api_key)



## main function 
def main():
    # 기본 설정
    st.set_page_config(
        page_title="Voice Chat-bot Program",
        layout="wide")
    
    # 제목
    st.header("Voice Chat-bot Program")

    # 구분선
    st.markdown("---")

    # 기본설명
    with st.expander("About Voice Chat-bot Program", expanded=False):
        st.write(
        """
        - Voice Chat-bot Program's UI uses Streamlit.
        - STT(Speech-To-Text) uses Whisper from OpenAI
        - Answer uses GPT model from OpenAI
        - TTS(Text-To-Speech) uses TTS from OpenAI
        """
        )
    
        st.markdown("")
    
    system_content = "You are a thoughful assistant. Response to all input in 25 words and answer in Korean"
    
    # session state 초기화
    if "chat" not in st.session_state:
         st.session_state["chat"] = []

    if "messages" not in st.session_state:
         st.session_state["messages"] = [{"role": "system", "content":system_content}]

    if "check_reset" not in st.session_state:
         st.session_state["check_reset"] = False

    # 사이드바 생성
    with st.sidebar:

        # gpt 모델을 선택하기 위한 라디오 버튼
        model = st.radio(label="GPT Models", options=["gpt-3.5 turbo", "gpt-4o", "gpt-4-turbo"])
        st.markdown("---")

        # 리셋 버튼 생성
        if st.button(label="Reset"):
            # 리셋 코드
            st.session_state["chat"] = []
            st.session_state["messages"] = [{"role":"system", "content": system_content}]
            st.session_state["check_reset"] = True

    # 기능 구현 공간
    col1, col2 = st.columns(2)
    with col1:
         #왼쪽 영역 작성
         st.subheader("Question")
    with col2:
         # 오른쪽 영역 설정
         st.subheader("QnA")

         
if __name__=="__main__":
        main()