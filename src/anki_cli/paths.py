from pathlib import Path

BASE_DIR = Path.home() / ".anki-cli"
QUEUE_FILE = BASE_DIR / "queue.txt"
HISTORY_FILE = BASE_DIR / "history.txt"
CONFIG_FILE = BASE_DIR / "config.txt"

DEFAULT_CONFIG = {
    "deck": "English",
    "model": "Basic",
    "context_model": "Basic",
    "tag": "vocab",
    "field_front": "",
    "field_back": ""
}


def ensure_files():
    BASE_DIR.mkdir(exist_ok=True)

    for file in [QUEUE_FILE, HISTORY_FILE]:
        if not file.exists():
            file.touch()


def ensure_config():
    BASE_DIR.mkdir(exist_ok=True)

    if not CONFIG_FILE.exists():
        with open(CONFIG_FILE, "w", encoding="utf-8") as f:
            f.write("# Anki CLI configuration\n\n")
            for key, value in DEFAULT_CONFIG.items():
                f.write(f"{key}={value}\n")