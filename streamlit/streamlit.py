import streamlit as st
import tempfile
from moviepy.editor import *
from pydub import AudioSegment


st.markdown(
    """
    # RakuRakugo
    """
)

st.header("Upload a video")

VIDEO_FILE = st.file_uploader("Choose a video...", type="mp4")
DURATION = 60 * 1000

if VIDEO_FILE is not None:
    st.video(VIDEO_FILE)

    TEMP_VIDEO_FILE = tempfile.NamedTemporaryFile(delete=False)
    TEMP_VIDEO_FILE.write(VIDEO_FILE.read())
    video = VideoFileClip(TEMP_VIDEO_FILE.name)
    st.write("hello")
    video = video.subclip(0, int(DURATION/1000))
    st.write("hello")
    TEMP_AUDIO_FILE = tempfile.NamedTemporaryFile(delete=False)
    audio = video.audio
    st.write("hello")
    audio.write_audiofile(TEMP_AUDIO_FILE.name, codec="pcm_s16le")
    st.write("hello")


    # output easified video
    st.header("Easified video")
    st.write("This will take a while...")
