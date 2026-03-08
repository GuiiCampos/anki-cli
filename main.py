import sys

from anki_cli.paths import ensure_files
from anki_cli import cli


def main():
    ensure_files()

    if len(sys.argv) < 2:
        print("Commands:")
        print(" add WORD")
        print(" addcard")
        print(" list")
        print(" remove INDEX")
        print(" clear")
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

    elif command == "open":
        cli.open_queue()

    elif command == "clear":
        cli.clear()

    else:
        print("Unknown command")


if __name__ == "__main__":
    main()