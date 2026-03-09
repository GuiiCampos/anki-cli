import requests # type: ignore

ANKI_URL = "http://127.0.0.1:8765"


def invoke(action, params=None):

    payload = {
        "action": action,
        "version": 6,
        "params": params or {}
    }

    response = requests.post(ANKI_URL, json=payload)

    return response.json()

def add_card(deck, front, back):

    params = {
        "note": {
            "deckName": deck,
            "modelName": "Basic",
            "fields": {
                "Front": front,
                "Back": back
            },
            "tags": ["anki-cli"]
        }
    }

    return invoke("addNote", params)