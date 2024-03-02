import os
from pathlib import Path
from dotenv import load_dotenv

dotenv_path = Path("__file__").resolve().parents[1].parents[0] / '.local.env'
load_dotenv(dotenv_path)


##################  FILE PATHS  ##################
DATA_PATH = Path("__file__").resolve().parents[1].parents[0] / "local_data"
USER_PATH = os.path.join(DATA_PATH, "user_input")

VIDEO_FILE_NAME = "rakugo_v1.mp4"
VIDEO_FILE_PATH = os.path.join(USER_PATH, VIDEO_FILE_NAME)
AUDIO_FILE_PATH = os.path.join(USER_PATH, "rakugo_v1.mp3")

##################  API KEYS  ##################
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
