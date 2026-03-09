from pathlib import Path

BASE_DIR = Path.home() / ".anki-cli"

QUEUE_FILE = BASE_DIR / "queue.txt"
HISTORY_FILE = BASE_DIR / "history.txt"
CONFIG_FILE = BASE_DIR / "config.txt"


def ensure_files():
    BASE_DIR.mkdir(exist_ok=True)

    for file in [QUEUE_FILE, HISTORY_FILE, CONFIG_FILE]:
        if not file.exists():
            file.touch()
