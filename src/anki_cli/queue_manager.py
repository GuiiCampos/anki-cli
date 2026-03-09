from .paths import QUEUE_FILE

def add_line(line):
    with open(QUEUE_FILE, "a", encoding="utf-8") as f:
        f.write(line + "\n")


def get_queue():
    with open(QUEUE_FILE, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f.readlines()]

    return [l for l in lines if l]


def save_queue(lines):
    with open(QUEUE_FILE, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line + "\n")


def remove_item(index):
    lines = get_queue()

    if index < 1 or index > len(lines):
        print("Invalid index")
        return

    removed = lines.pop(index - 1)
    save_queue(lines)

    print(f"Removed: {removed}")


def update_item(index, new_line):
    lines = get_queue()

    if index < 1 or index > len(lines):
        print("Invalid index")
        return False

    lines[index - 1] = new_line
    save_queue(lines)

    return True


def clear_queue():
    save_queue([])