import os
import sys
import json
import requests
import argparse  # For command-line arguments (optional)
import logging  # For suppressing gRPC warning (optional)

ANKI_CONNECT_URL = 'http://localhost:8765'  # Default AnkiConnect URL

def anki_connect_request(action, params=None): # Modified: params now explicitly as argument
    """
    Makes a request to AnkiConnect API.
    (Trying explicit positional argument JSON for createDeck - Attempt 4)
    """
    request_payload = {'action': action, 'version': 6} # Start with action and version
    if params is not None: # Add params only if provided
        request_payload['params'] = params # Explicitly set params

    requestJson = json.dumps(request_payload)
    headers = {'Content-Type': 'application/json'} # Explicitly set header
    print(f"DEBUG: Sending JSON request: {requestJson}")
    try:
        response = requests.post(ANKI_CONNECT_URL, requestJson, headers=headers).json()
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to AnkiConnect. Is Anki running with AnkiConnect add-on installed and enabled?")
        return None
    print(f"DEBUG: Received JSON response: {response}")
    if len(response) != 2:
        raise Exception('response has an unexpected number of fields')
    if 'error' not in response:
        raise Exception('response is missing required error field')
    if 'result' not in response:
        raise Exception('response is missing required result field')
    if response['error'] is not None:
        raise Exception(response['error'])
    return response['result']

def create_deck_if_not_exists(deck_name):
    """
    Creates an Anki deck if it does not already exist.
    (Attempt 4 - Explicit positional argument JSON construction)
    """
    deck_names = anki_connect_request('deckNames')
    if deck_names is None:
        return None
    if deck_name not in deck_names:
        # Modified line: Explicitly constructing positional argument JSON
        deck_id = anki_connect_request('createDeck', params={'deck': deck_name}) # params as DICT with 'deck' key
        if deck_id is None:
            return None
        print(f"Created new deck: '{deck_name}' (id: {deck_id})")
        return deck_id
    else:
        deck_id = anki_connect_request('deckNamesAndIds').get(deck_name)
        print(f"Using existing deck: '{deck_name}' (id: {deck_id})")
        return deck_id

def get_model_names():
    """
    Gets a list of available note model names from Anki.
    """
    return anki_connect_request('modelNames')

def get_tags():
    """
    Gets a list of existing tags from Anki.
    """
    return anki_connect_request('getTags')

def add_note_to_anki(deck_name, model_name, fields, tags):
    """
    Adds a note to Anki using AnkiConnect.
    (Attempt 2 for addNote - Wrap the entire 'note' dictionary inside 'params')
    """
    note = { # note dictionary remains the same
        "deckName": deck_name,
        "modelName": model_name,
        "fields": fields,
        "tags": tags
    }
    # Modified line: Wrap the entire 'note' dictionary inside 'params'
    return anki_connect_request('addNote', params={'note': note}) # Wrap 'note' in a dictionary with key 'note'

def generate_anki_cards_from_file_anki_connect(input_file_path, deck_name="IELTS Cambridge"):
    """
    Generates Anki flashcards from a formatted text file and imports them into Anki using AnkiConnect.
    """

    try:
        with open(input_file_path, "r", encoding="utf-8") as f:
            card_data_text = f.read()
    except FileNotFoundError:
        print(f"Error: Input file not found at '{input_file_path}'.")
        return False 
    except Exception as e:
        print(f"Error reading input file: {e}")
        return False 

    card_blocks = card_data_text.strip().split("---\n")
    if not card_blocks or not any(block.strip() for block in card_blocks):
        print("Warning: No card data found in the input file.")
        return False 

    # --- Deck Setup using AnkiConnect ---
    deck_id = create_deck_if_not_exists(deck_name)
    if deck_id is None:
        return False

    # --- Model Check ---
    model_names = get_model_names()
    if model_names is None:
        return False
    model_name = "Basic" # Assuming "Basic" note type exists
    if model_name not in model_names:
        print(f"Error: '{model_name}' note model not found in Anki.")
        return False

    # --- Label Handling ---
    existing_labels = get_tags() or [] # Get existing tags, default to empty list if error
    print("\n--- Available Labels ---")
    for i, label in enumerate(existing_labels):
        print(f"{i+1}. {label}")
    print(f"{len(existing_labels) + 1}. New label")
    print("----------------------")

    while True:
        choice = input(f"Choose a label for these cards (1-{len(existing_labels) + 1}): ")
        try:
            choice_index = int(choice)
            if 1 <= choice_index <= len(existing_labels):
                selected_label = existing_labels[choice_index - 1]
                break
            elif choice_index == len(existing_labels) + 1:
                selected_label = input("Enter new label name: ").strip()
                if not selected_label:
                    print("Label name cannot be empty. Please try again.")
                    continue
                break
            else:
                print("Invalid choice. Please enter a number from the list.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    print(f"Selected label: '{selected_label}'")
    label_to_add = selected_label

    # --- Card Creation and Import using AnkiConnect ---
    print("\nCreating and importing Anki cards using AnkiConnect...")
    card_count = 0
    for block in card_blocks:
        block = block.strip()
        if not block:
            continue

        card_fields = {}
        for line in block.strip().split("\n"):
            if ":" in line:
                key, value = line.split(":", 1)
                card_fields[key.strip()] = value.strip()

        if "Front" in card_fields and "Back" in card_fields:
            fields_data = {
                "Front": card_fields.get("Front", ""),
                "Back": "" # Back content will be built below
            }
            back_content = ""
            #--- HTML Formatted Back Content ---
            if "Pronunciation" in card_fields:
                back_content += f"Pronunciation: {card_fields.get('Pronunciation', '')}<br><br>"
            if "Form" in card_fields:
                back_content += f"Form: {card_fields.get('Form', '')}<br><br>"
            if "Word Family" in card_fields:
                back_content += f"Word Family: {card_fields.get('Word Family', '')}<br><br>"
            back_content += f"English Meaning: {card_fields.get('English Meaning', '')}<br><br>" if "English Meaning" in card_fields else ""
            back_content += f"Vietnamese Meaning: {card_fields.get('Vietnamese Meaning', '')}<br><br>" if "Vietnamese Meaning" in card_fields else ""
            back_content += f"Example Sentence: {card_fields.get('Example Sentence', '')}" if "Example Sentence" in card_fields else "" # No <br> after last item

            fields_data["Back"] = back_content.strip()

            note_id = add_note_to_anki(deck_name, model_name, fields_data, [label_to_add])
            if note_id:
                card_count += 1
            else:
                print(f"Warning: Error adding note to Anki for block: {block[:50]}...") # Error adding note
        else:
            print(f"Warning: Incomplete card data in block, skipping: {block[:50]}...") # Incomplete card data
    
    print(f"\nSuccessfully imported {card_count} cards into Anki deck '{deck_name}' with label '{label_to_add}' using AnkiConnect.")

    return True # ADDED: Return True on successful completion

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate Anki cards from a text file using AnkiConnect.")
    parser.add_argument("input_file", help="Path to the input text file (.txt)")
    parser.add_argument("--deck", default="IELTS Cambridge", help="Name of the Anki deck (default: IELTS Cambridge)")

    args = parser.parse_args()

    if not args.input_file.lower().endswith(".txt"):
        print("Error: Input file must be a .txt file.")
    else:
        logging.getLogger('absl').setLevel(logging.ERROR) # ADDED: Suppress gRPC warning here
        generate_anki_cards_from_file_anki_connect(args.input_file, args.deck)