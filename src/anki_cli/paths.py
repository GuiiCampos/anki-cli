import shutil
from pathlib import Path

BASE_DIR = Path.home() / ".anki-cli"

QUEUE_FILE = BASE_DIR / "queue.txt"
HISTORY_FILE = BASE_DIR / "history.txt"
CONFIG_FILE = BASE_DIR / "config.txt"


def ensure_files():
    BASE_DIR.mkdir(exist_ok=True)

    for file in [QUEUE_FILE, HISTORY_FILE]:
        if not file.exists():
            file.touch()


EXAMPLE_CONFIG = Path(__file__).resolve().parents[2] / "config.example.txt"

def ensure_config():

    if not CONFIG_FILE.exists():
        shutil.copy(EXAMPLE_CONFIG, CONFIG_FILE)