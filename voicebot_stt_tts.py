import streamlit as st

# 나를 위한 함수를 정의 # ctrl + tab (들여쓰기) <-> Shift + tab (빼기)
def main():
    st.set_page_config(page_title="음성 챗봇", layout="wide")

    # 제목
    st.header("음성 챗봇 프로그램")

    # 구분선 만들기
    st.markdown("---")
    with st.expander("음성 챗봇 프로그램에 관하여", expanded=True): 
        st.write(
            """ 
            - 음성 번역 챗봇 프로그램의 UI는 Streamlit을 활용합니다.
            - STT(Speech-To-Text)는 OpenAI의 Whisper를 활용합니다. 
            - 답변은 OpenAI의 GPT 모델을 활용합니다. 
            - TTS(Text-To-Speech)는 OpenAI의 TTS를 활용합니다.
            """
        )

        st.markdown("")

if __name__ == "_main_":
# 실행 함수
    main()

# 터미널 웹 페이지 실행  스탑하려면 ctrl + c