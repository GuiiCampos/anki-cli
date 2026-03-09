import sys

from anki_cli.paths import ensure_files, ensure_config
from anki_cli import cli
from anki_cli.anki_connect import invoke


def main():
    ensure_config()
    ensure_files()

    print(invoke("deckNames"))

    if len(sys.argv) < 2:
        cli.show_help()
        return

    command = sys.argv[1]

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

    elif command == "open":
        cli.open_queue()

    elif command == "history":
        cli.open_history()
    
    elif command == "config":
        cli.open_config()
    
    elif command in ["help", "--help"]:
        cli.show_help()

    elif command == "clear":
        cli.clear()

    else:
        print("Unknown command")


if __name__ == "__main__":
    main()