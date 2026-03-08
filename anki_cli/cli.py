from .queue_manager import add_line, get_queue, remove_item, clear_queue


def add(word):
    add_line(word)
    print(f"Added: {word}")


def addcard():
    word = input("Word: ").strip()
    translation = input("Translation: ").strip()
    card_type = input("Type (t/c): ").strip()
    example = input("Example: ").strip()

    line = f"{word}|{translation}|{card_type}|{example}"
    add_line(line)

    print("Card added to queue.")


def list_queue():
    lines = get_queue()

    if not lines:
        print("Queue empty")
        return

    for i, line in enumerate(lines, start=1):
        print(f"{i}  {line}")


def remove(index):
    remove_item(index)


def clear():
    clear_queue()
    print("Queue cleared")
