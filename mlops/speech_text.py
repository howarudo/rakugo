from pathlib import Path
import pytube as pt
from openai import OpenAI
import os
from dotenv import load_dotenv

dotenv_path = Path("__file__").resolve().parents[1].parents[0] / '.local.env'
load_dotenv(dotenv_path)

OpenAI.api_key = os.getenv("OPENAI_API_KEY")
data_path = Path("__file__").resolve().parents[1].parents[0] / "local_data"
