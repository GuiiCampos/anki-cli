import sys
from pathlib import Path

# pasta do usuário
BASE_DIR = Path.home() / ".anki-cli"
QUEUE_FILE = BASE_DIR / "queue.txt"
HISTORY_FILE = BASE_DIR / "history.txt"


def ensure_files():
    BASE_DIR.mkdir(exist_ok=True)

    if not QUEUE_FILE.exists():
        QUEUE_FILE.touch()

    if not HISTORY_FILE.exists():
        HISTORY_FILE.touch()


def add_word(word):
    with open(QUEUE_FILE, "a", encoding="utf-8") as f:
        f.write(word + "\n")

    print(f"Added: {word}")


def list_queue():
    with open(QUEUE_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()

    if not lines:
        print("Queue is empty.")
        return

    for i, line in enumerate(lines, start=1):
        print(f"{i}  {line.strip()}")


def remove_item(index):
    with open(QUEUE_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()

    if index < 1 or index > len(lines):
        print("Invalid index.")
        return

    removed = lines.pop(index - 1)

    with open(QUEUE_FILE, "w", encoding="utf-8") as f:
        f.writelines(lines)

    print(f"Removed: {removed.strip()}")


def clear_queue():
    open(QUEUE_FILE, "w").close()
    print("Queue cleared.")


def main():
    ensure_files()

    if len(sys.argv) < 2:
        print("Usage:")
        print("  add WORD")
        print("  list")
        print("  remove INDEX")
        print("  clear")
        return

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 3:
            print("Usage: add WORD")
            return
        add_word(sys.argv[2])

    elif command == "list":
        list_queue()

    elif command == "remove":
        if len(sys.argv) < 3:
            print("Usage: remove INDEX")
            return
        remove_item(int(sys.argv[2]))

    elif command == "clear":
        clear_queue()

    else:
        print("Unknown command")


if __name__ == "__main__":
    main()