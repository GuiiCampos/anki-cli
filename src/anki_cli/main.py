import sys
import time

from .paths import ensure_files, ensure_config
from . import cli
from .anki_connect import AnkiConnectionError, is_connected, get_model_fields, detect_basic_model
from .config import load_config, save_config


def detect_fields():
    config = load_config()

    if config.get("field_front") and config.get("field_back"):
        return

    print("\nConfiguração inicial necessária.")
    print("Por favor, abra o Anki e pressione Enter para continuar...")
    input()

    while True:
        print("Conectando ao Anki...")

        if is_connected():
            break

        print("Não foi possível conectar. Verifique se o Anki está aberto e tente novamente.")
        input("Pressione Enter para tentar novamente...")

    model = detect_basic_model()
    if not model:
        print("Modelo Basic/Básico não encontrado no anki.")
        return
    
    fields = get_model_fields(model)
    if len(fields) < 2:
        print(f"Não foi possível detectar os campos do modelo '{model}'.")
        return

    config["model"] = model
    config["context_model"] = model
    config["field_front"] = fields[0]
    config["field_back"] = fields[1]
    save_config(config)

    print(f"Campos detectados: {fields[0]}, {fields[1]}, {model}")
    print("Configuração salva!\n")



def main():
    ensure_config()
    ensure_files()
    detect_fields()

    if len(sys.argv) < 2:
        cli.show_help()
        return

    command = sys.argv[1]

    try:
        run(command)
    except AnkiConnectionError as e:
        print(f"Error: {e}")


def run(command):
    if command == "add":
        cli.add(sys.argv[2])

    elif command == "addcard":
        cli.addcard()

    elif command == "list":
        cli.list_queue()

    elif command == "remove":
        cli.remove(int(sys.argv[2]))

    elif command == "edit":
        if len(sys.argv) < 3:
            print("Usage: edit INDEX")
            return
        cli.edit(int(sys.argv[2]))

    elif command == "process":
        cli.process()

    elif command == "status":
        cli.status()

    elif command == "open":
        cli.open_one_dir("queue")

    elif command == "history":
        cli.open_one_dir("history")
    
    elif command == "config":
        cli.open_one_dir("config")

    elif command == "deck":
        if len(sys.argv) < 3:
            print("Usage: anki deck <change|new>")
            return
        
        subcommand = sys.argv[2]
        if subcommand == "change":
            cli.change_deck()
        elif subcommand == "new":
            cli.deck_new()
        else:
            print(f"Unknown subcommand: {subcommand}")

    elif command in ["help", "--help"]:
        cli.show_help()

    elif command == "clear":
        cli.clear()

    else:
        print("Unknown command")


if __name__ == "__main__":
    main()