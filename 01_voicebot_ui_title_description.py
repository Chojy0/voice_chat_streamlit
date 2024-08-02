# Streamlit 패키지 추가
# pip install streamlit
# streamlit 실행 : streamlit run app.py
import streamlit as st

##### 메인 함수 #####
def main():
    # 페이지 타이틀 설정
    st.set_page_config(page_title="음성 챗봇 프로그램", layout="wide")

    # 제목 
    st.header("음성 챗봇 프로그램")

    # 구분선
    st.markdown("---")    

    # 기본 설명
    with st.expander("음성 챗봇 프로그램에 관하여", expanded=True):
        st.write(
        """     
        - 음성 번역 챗봇 프로그램의 UI는 스트림릿을 활용합니다.
        - STT(Speech-To-Text)는 OpenAI의 Whisper를 활용합니다. 
        - 답변은 OpenAI의 GPT 모델을 활용합니다. 
        - TTS(Text-To-Speech)는 OpenAI의 TTS를 활용합니다.
        """
        )

        st.markdown("")

if __name__=="__main__":
    main()