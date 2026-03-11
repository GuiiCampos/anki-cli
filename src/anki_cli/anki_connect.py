import requests # type: ignore

ANKI_URL = "http://127.0.0.1:8765"


class AnkiConnectionError(Exception):
    pass


def invoke(action, params=None):
    payload = {
        "action": action,
        "version": 6,
        "params": params or {}
    }

    try:
        response = requests.post(ANKI_URL, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.ConnectionError:
        raise AnkiConnectionError("Could not connect to Anki. Is it open?")
    except requests.exceptions.RequestException as e:
        raise AnkiConnectionError(f"Anki request failed: {e}")
    

def add_card(deck, front, back, model="Basic"):
    params = {
        "note": {
            "deckName": deck,
            "modelName": model,
            "fields": {
                "Front": front,
                "Back": back
            },
            "tags": ["anki-cli"]
        }
    }
    return invoke("addNote", params)


def get_decks():
    result = invoke("deckNames")
    return result.get("result", [])


def create_deck(name):
    result = invoke("createDeck", {"deck": name})
    return result.get("result")