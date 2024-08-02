# # Streamlit을 사용하여 음성 기반 챗봇 프로그램 만들기 예제
# # 여기서는 OpenAI의 Whisper 모델을 사용하여 음성을 텍스트로 변환(STT: Speech-To-Text)하고, 
# # 변환된 텍스트를 기반으로 GPT 모델을 사용하여 답변을 생성합니다. 

# # Streamlit 패키지 추가
# import streamlit as st

# # OpenAI 패키지 추가
# import openai

# import os
# from dotenv import load_dotenv

# # .env 파일 경로 지정 
# load_dotenv()

# # audiorecorder 패키지 추가 :  Streamlit 애플리케이션에서 오디오를 녹음할 수 있는 컴포넌트를 제공
# # pip install streamlit-audiorecorder

# from audiorecorder import audiorecorder

# # Open AI API 키 설정하기
# api_key = os.environ.get('OPENAI_API_KEY')

# client = openai.OpenAI(api_key=api_key)

# ##### 메인 함수 #####
# def main():
#     # 기본 설정
#     st.set_page_config(
#         page_title="음성 챗봇 프로그램",
#         layout="wide")

#     # 제목 
#     st.header("음성 챗봇 프로그램")

#     # 구분선
#     st.markdown("---")

#     # 기본 설명
#     with st.expander("음성 챗봇 프로그램에 관하여", expanded=True):
#         st.write(
#         """     
#         - 음성 번역 챗봇 프로그램의 UI는 스트림릿을 활용합니다.
#         - STT(Speech-To-Text)는 OpenAI의 Whisper를 활용합니다. 
#         - 답변은 OpenAI의 GPT 모델을 활용합니다. 
#         - TTS(Text-To-Speech)는 OpenAI의 TTS를 활용합니다.
#         """
#         )

#         st.markdown("")
    
#     system_content = "You are a thoughtful assistant. Respond to all input in 25 words and answer in korea"

#     # session state 초기화
#     if "chat" not in st.session_state:
#         st.session_state["chat"] = []

#     if "messages" not in st.session_state:
#         st.session_state["messages"] = [{"role": "system", "content": system_content}]

#     if "check_reset" not in st.session_state:
#         st.session_state["check_reset"] = False

#     # 사이드바 생성
#     with st.sidebar:

#         # GPT 모델을 선택하기 위한 라디오 버튼
#         model = st.radio(label="GPT 모델", options=["gpt-3.5-turbo", "gpt-4o", "gpt-4-turbo"])

#         st.markdown("---")

#         # 리셋 버튼 생성
#         if st.button(label="초기화"):
#             # 리셋 코드 
#             st.session_state["chat"] = []
#             st.session_state["messages"] = [{"role": "system", "content": system_content}]
#             st.session_state["check_reset"] = True

#     # 기능 구현 공간
#     col1, col2 = st.columns(2)
#     with col1:
#         # 왼쪽 영역 작성
#         st.subheader("질문하기")

#         # 음성 녹음 아이콘 추가
#         audio = audiorecorder()
#         if (audio.duration_seconds > 0) and (st.session_state["check_reset"]==False):
#             # 음성 재생 
#             st.audio(audio.export().read())

#     with col2:
#         # 오른쪽 영역 작성
#         st.subheader("질문/답변")

# if __name__=="__main__":
#     main()

# gpt40버전
import streamlit as st
import openai
import os
from dotenv import load_dotenv
from datetime import datetime
from streamlit_webrtc import webrtc_streamer, WebRtcMode, ClientSettings
import av
import numpy as np
import pydub

# .env 파일 경로 지정 
load_dotenv()

# Open AI API 키 설정하기
api_key = os.environ.get('OPENAI_API_KEY')
openai.api_key = api_key

##### 기능 구현 함수 #####
def STT(audio_data):
    # 파일 저장
    filename = 'input.wav'
    with open(filename, 'wb') as f:
        f.write(audio_data)

    # 음원 파일 열기
    with open(filename, "rb") as audio_file:
        # Whisper 모델을 활용해 텍스트 얻기
        transcription = openai.Audio.transcribe(
            model="whisper-1", 
            file=audio_file
        )

    # 파일 삭제
    os.remove(filename)
    
    return transcription['text']

##### 메인 함수 #####
def main():
    # 기본 설정
    st.set_page_config(
        page_title="음성 챗봇 프로그램",
        layout="wide")

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

    system_content = "You are a thoughtful assistant. Respond to all input in 25 words and answer in Korea."

    # session state 초기화
    if "chat" not in st.session_state:
        st.session_state["chat"] = []

    if "messages" not in st.session_state:
        st.session_state["messages"] = [{"role": "system", "content": system_content}]

    if "check_reset" not in st.session_state:
        st.session_state["check_reset"] = False

    # 사이드바 생성
    with st.sidebar:

        # GPT 모델을 선택하기 위한 라디오 버튼
        model = st.radio(label="GPT 모델", options=["gpt-3.5-turbo", "gpt-4", "gpt-4-turbo"])

        st.markdown("---")

        # 리셋 버튼 생성
        if st.button(label="초기화"):
            # 리셋 코드 
            st.session_state["chat"] = []
            st.session_state["messages"] = [{"role": "system", "content": system_content}]
            st.session_state["check_reset"] = True

    # 기능 구현 공간
    col1, col2 = st.columns(2)
    with col1:
        # 왼쪽 영역 작성
        st.subheader("질문하기")

        # 음성 녹음 아이콘 추가
        webrtc_ctx = webrtc_streamer(
            key="example",
            mode=WebRtcMode.SENDRECV,
            client_settings=ClientSettings(
                rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]},
                media_stream_constraints={"audio": True, "video": False},
            ),
        )

        if webrtc_ctx.audio_receiver and st.session_state["check_reset"] == False:
            audio_frames = webrtc_ctx.audio_receiver.get_frames()
            if len(audio_frames) > 0:
                audio = audio_frames[-1]
                sound = pydub.AudioSegment(
                    audio.to_ndarray().tobytes(), 
                    frame_rate=audio.sample_rate,
                    sample_width=audio.sample_width,
                    channels=1
                )

                audio_data = sound.export(format="wav").read()
                question = STT(audio_data)

                # 채팅을 시각화하기 위해 질문 내용 저장
                now = datetime.now().strftime("%H:%M")
                st.session_state["chat"] = st.session_state["chat"] + [("user", now, question)]

                # GPT 모델에 넣을 프롬프트를 위해 질문 내용 저장
                st.session_state["messages"] = st.session_state["messages"] + [{"role": "user", "content": question}]

    with col2:
        # 오른쪽 영역 작성
        st.subheader("질문/답변")

if __name__ == "__main__":
    main()
