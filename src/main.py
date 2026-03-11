import sys

from anki_cli.paths import ensure_files, ensure_config
from anki_cli import cli
from anki_cli.anki_connect import AnkiConnectionError

def main():
    ensure_config()
    ensure_files()

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