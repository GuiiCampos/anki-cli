from .queue_manager import add_line, get_queue, remove_item, clear_queue
from .queue_manager import update_item

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


def edit(index):
    lines = get_queue()

    if index < 1 or index > len(lines):
        print("Invalid index")
        return

    current = lines[index - 1]

    print(f"Current: {current}")

    parts = current.split("|")

    # verifica se tem 4 campos
    while len(parts) < 4:
        parts.append("")

    word, translation, card_type, example = parts

    new_word = input(f"Word ({word}): ").strip() or word
    new_translation = input(f"Translation ({translation}): ").strip() or translation
    new_type = input(f"Type ({card_type}): ").strip() or card_type
    new_example = input(f"Example ({example}): ").strip() or example

    new_line = f"{new_word}|{new_translation}|{new_type}|{new_example}"

    success = update_item(index, new_line)

    if success:
        print("Item updated.")


def clear():
    clear_queue()
    print("Queue cleared")