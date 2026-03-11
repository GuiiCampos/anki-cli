import os

from datetime import datetime
from .paths import HISTORY_FILE, QUEUE_FILE, CONFIG_FILE
from .queue_manager import add_line, get_queue, remove_item, clear_queue, update_item
from .anki_connect import add_card, get_decks
from .config import load_config, save_config

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


def open_one_dir(value):
    paths = {
        "queue": str(QUEUE_FILE),
        "history": str(HISTORY_FILE),
        "config": str(CONFIG_FILE),
    }

    path = paths.get(value)
    
    if not path:
        print(f"Unknown file: {value}")
        return
    
    if os.name == "nt":
        os.startfile(path)
    else:
        os.system(f"xdg-open {path}")


def show_help():
    print("""
Anki CLI - Gerenciador de fila e criação rápida de flashcards

    USO:
        anki [COMMANDS] [ARGUMENTS]

    COMMANDS:
        add <word>        Adiciona uma palavra rapidamente à fila
        addcard           Criação interativa de cartões
        list              Exibe os itens da fila
        edit <index>      Edita um item específico da fila
        remove <index>    Remove um item da fila
        clear             Limpa toda a fila
        open              Abre o arquivo (queue.txt)
        history           Abre o histórico (history.txt)
        config            Abre o arquivo de configuração (config.txt)
        process           Processa a fila e gera os flashcards
        change-deck       Muda o deck usado para enviar os cards        
        help              Mostra esta mensagem de ajuda

    Exemplos:
        anki add hold
        anki edit 2
""")


def clear():
    clear_queue()
    print("Queue cleared")

## Sobre a lógica envolvendo o process ->

def parse_line(line):
    parts = line.split("|")

    while len(parts) < 4:
        parts.append("")

    word, translation, card_type, example = parts

    return word, translation, card_type, example


def complete_fields(word, translation, card_type, example):

    if not translation:
        translation = input(f"Translation for '{word}': ").strip()

    if not card_type:
        card_type = input("Type (t/c): ").strip()

    if card_type == "c" and not example:
        example = input("Example sentence: ").strip()

    return word, translation, card_type, example


def save_history(word, translation, card_type, example):
    date = datetime.now().strftime("%Y-%m-%d")

    line = f"{date}|{word}|{translation}|{card_type}|{example}"

    with open(HISTORY_FILE, "a", encoding="utf-8") as f:
        f.write(line + "\n")


def process():
    queue = get_queue()

    config = load_config()
    deck = config["deck"]

    if not queue:
        print("Queue is empty.")
        return

    print(f"Processing {len(queue)} items\n")

    for line in queue:

        word, translation, card_type, example = parse_line(line)

        print(f"\nWord: {word}")

        word, translation, card_type, example = complete_fields(
            word, translation, card_type, example
        )
        
        if card_type == "t":
            front = word
            back = translation
            model = config["model"]
        elif card_type == "c":
            front = f"{example}<br><br>What does '{word}' mean?"
            back = translation
            model = config["context_model"]
        else:
            print(f"Unknown card type: {card_type}")
            continue

        add_card(deck, front, back, model)
        save_history(word, translation, card_type, example)
        print("Saved.")
    
    clear_queue()
    print("\nQueue cleared.")


def change_deck():
    decks = get_decks()

    if not decks:
        print("No decks found. Is Anki open?")
        return
    
    print("\nAvailable decks:\n")
    for i, deck in enumerate(decks, 1):
        print(f"{i}. {deck}")

    config = load_config()
    print(f"\nCurrent deck: {config['deck']}")

    choice = input("\nSelect deck number: ").strip()

    try:
        selected = decks[int(choice) - 1]
    except:
        print("Invalid option.")
        return
 
    config["deck"] = selected
    save_config(config)
    print(f"\nDeck changed to: {selected}")