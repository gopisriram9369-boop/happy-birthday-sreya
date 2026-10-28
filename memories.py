import json
from pathlib import Path

DATA_FILE = Path(__file__).with_name("memories.json")

def get_photos():
    return json.loads(DATA_FILE.read_text(encoding="utf-8"))
