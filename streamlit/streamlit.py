import streamlit as st
from pathlib import Path
import tempfile
from moviepy.editor import *
from pydub import AudioSegment
from openai import OpenAI
from dotenv import load_dotenv

dotenv_path = Path("__file__").resolve().parents[0] / '.local.env'
load_dotenv(dotenv_path)

OpenAI.api_key = os.getenv("OPENAI_API_KEY")
data_path = Path("__file__").resolve().parents[0] / "local_data"


st.markdown(
    """
    # RakuRakugo
    """
)

st.header("Upload a video")

uploaded_video = st.file_uploader("Choose a video...", type="mp4")
uploaded_audio = st.file_uploader("Choose an audio...", type="mp3")

if uploaded_video is not None and uploaded_audio is not None:
    st.video(uploaded_video)
    video_bytes_data = uploaded_video.getvalue()
    audio_bytes_data = uploaded_audio.getvalue()

    with open("user_input.mp4", 'wb') as f:
        f.write(video_bytes_data)

    with open("user_input.mp3", 'wb') as f:
        f.write(audio_bytes_data)

    duration = 60 * 1000
    video = VideoFileClip("user_input.mp4")
    video = video.subclip(0, int(duration/1000))

    audio = AudioSegment.from_file("user_input.mp3", format="mp3")
    audio = audio[:duration]

    client = OpenAI()

    audio_file = open("user_input.mp3", "rb")

    transcript = client.audio.transcriptions.create(
        file=audio_file,
        model="whisper-1",
        response_format="verbose_json",
        timestamp_granularities=["segment"]
    )

    import re

    segments = []
    for segment in transcript.segments:
        text = re.sub(r'[a-zA-Z0-9🎶]', '', segment["text"]).strip()
        start = segment["start"]
        end = segment["end"]

        if text and (end-start) > 2.5:
            segments.append({
                "text": text,
                "start": start,
                "end": end
            })

    sentences = [segment["text"] for segment in segments]

    input_text = "\n".join([f"{i+1}. {sentence}" for i, sentence in enumerate(sentences)])
    st.write(input_text)
    JLPT_LEVEL = "N4"


    completion = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": """
        日本の落語の一節と日本語能力試験（JLPT）のレベルが与えられます。\n
        その節を、指定されたJLPTレベルに適した語彙を使って簡単にしてください。\n
        語彙のみを変更してください。文の構造や意味は変更しないでください。\n
        """},
        {"role": "user", "content": f"""
        JLPTレベル: {JLPT_LEVEL}\n
        落語の節:\n
        {input_text}
        """}
    ]
    )

    completion_output = completion.choices[0].message.content
    import re

    easified_sentences = re.findall(r"\d+\. (.+)", completion_output)
    st.write(easified_sentences)

    ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
    audio_file_paths = ["user_input.mp3"]

    from elevenlabs import clone, generate

    voice = clone(
        api_key=ELEVENLABS_API_KEY,
        name="rakugo_v1",
        files=audio_file_paths,
    )


    audios = []
    for sentence in easified_sentences:
        audio = generate(
            api_key=ELEVENLABS_API_KEY,
            text=sentence,
            voice=voice,
            model="eleven_multilingual_v2",
            output_format="mp3_44100_128"
        )
        audios.append(audio)
    # output easified video

    temp_res_file_path = os.path.join(data_path, "temp_results")
    os.makedirs(temp_res_file_path, exist_ok=True)

    # save generated audio to mp3
    for i, audio in enumerate(audios):
        audio_file_path = os.path.join(temp_res_file_path, f"rakugo_v1_{i}.mp3")
        with open(audio_file_path, "wb") as f:
            f.write(audio)
        st.write(f"audio file saved to {audio_file_path}")

    from pydub import AudioSegment
    from pydub.effects import speedup

    for i, segment in enumerate(segments):
        audio_file_path = os.path.join(temp_res_file_path, f"rakugo_v1_{i}.mp3")
        audio = AudioSegment.from_file(audio_file_path, format="mp3")
        audio_dur = len(audio) / 1000
        speed = audio_dur / (segment['end'] - segment['start'])
        st.write("original audio duration", audio_dur, "segment duration", segment['end'] - segment['start'], "speed", speed)
        # round speed to nearest from 1, 1.25, 1.5
        speed = round(speed*4) / 4
        if speed <= 1:
            speed = 1
            speeded_audio = audio
        else:
            speeded_audio = speedup(audio, speed)
        st.write(f"speeded audio with speed {speed}")
        speeded_audio.export(os.path.join(temp_res_file_path, f"rakugo_v1_{i}_speeded.mp3"), format="mp3")
        st.write(f"audio file saved")


    for i, segment in enumerate(segments):
        audio_file_path = os.path.join(temp_res_file_path, f"rakugo_v1_{i}_speeded.mp3")
        original_audio_file_path = "user_input.mp3"
        original_audio = AudioSegment.from_file(original_audio_file_path, format="mp3")
        audio = AudioSegment.from_file(audio_file_path, format="mp3")
        current_time = segment['start'] * 1000
        st.write("current_time", current_time, "segment start", segment['start'], "segment end", segment['end'])
        if i == 0:
            fill_dur = current_time
            fill = original_audio[:fill_dur]
            merged_audio = fill + audio
        else:
            silence_dur = segment['start'] * 1000 - current_time
            silence = AudioSegment.silent(duration=silence_dur)
            merged_audio = merged_audio + silence + audio
        current_time = len(merged_audio)

    merged_audio.export(os.path.join(temp_res_file_path, f"rakugo_v1_merged.mp3"), format="mp3")

    import moviepy.editor as mp

    final_res_file_path = os.path.join(data_path, "final_results")

    audio = mp.AudioFileClip(os.path.join(temp_res_file_path, "rakugo_v1_merged.mp3"))
    video1 = mp.VideoFileClip("user_input.mp4")
    final = video1.set_audio(audio)

    final.write_videofile(os.path.join(final_res_file_path, "rakugo_v1_final.mp4"))

    st.video(os.path.join(final_res_file_path, "rakugo_v1_final.mp4"))

    st.header("Easified video")
    st.write("This will take a while...")
