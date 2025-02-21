import os
import sys
# --- Import functions from your existing scripts ---
from api_connect import setup_gemini_api  # Assuming api_connect.py is in the same directory
from input_processing import analyze_ielts_passage, format_gemini_output_to_anki_v6 # Assuming input_processing.py is in the same directory
from generate_anki_cards import generate_anki_cards_from_file_anki_connect # Assuming generate_anki_cards.py is in the same directory

def process_ielts_passage_and_create_anki_cards(ielts_passage_text, output_file="anki_cards_output.txt", deck_name="IELTS Cambridge", card_label=None): # Added card_label argument
    """
    Orchestrates the process of analyzing an IELTS passage, formatting Anki cards,
    and importing them into Anki.

    Args:
        ielts_passage_text (str): The IELTS reading passage text.
        output_file (str, optional): Path to save the intermediate Anki card output. Defaults to "anki_cards_output.txt".
        deck_name (str, optional): Name of the Anki deck to import into. Defaults to "IELTS Cambridge".

    Returns:
        bool: True if the entire process was successful, False otherwise.
    """
    print("--- Starting IELTS Passage Analysis and Anki Card Generation ---")

    # 1. Setup Gemini API (already setup in api_connect, just need to ensure it initializes)
    print("Setting up Gemini API...")
    gemini_model = setup_gemini_api()
    if not gemini_model:
        print("Gemini API setup failed. Aborting.")
        return False
    print("Gemini API setup successful!")

    # 2. Analyze IELTS Passage using Gemini and format for Anki
    print("Analyzing IELTS Passage and Formatting Anki Cards...")
    anki_card_output_string = analyze_ielts_passage(ielts_passage_text) # Assuming V6 formatting is desired
    if not anki_card_output_string:
        print("IELTS Passage analysis and Anki card formatting failed. Aborting.")
        return False

    # 3. Save Anki card output to a text file (intermediate step)
    print(f"Saving Anki card output to: {output_file}")
    try:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(anki_card_output_string)
    except Exception as e:
        print(f"Error saving Anki card output to file: {e}. Aborting.")
        return False
    print(f"Anki card output saved to: {output_file}")

    # 4. Generate Anki cards from the text file and import into Anki
    print("Generating Anki cards and Importing into Anki...")
    if not generate_anki_cards_from_file_anki_connect(output_file, deck_name, card_label=card_label): # Pass card_label here
        print("Anki card generation and import failed. Check errors from generate_anki_cards.py.")
        return False
    print(f"Anki card generation and import into deck '{deck_name}' successful!")

    print("--- IELTS Passage Analysis and Anki Card Generation Process Completed Successfully! ---")
    return True


if __name__ == "__main__":
    # --- Example Usage from Command Line (for testing main.py itself) ---
    example_passage = """
    The concept of 'emotional intelligence' (EQ) has gained considerable traction in recent years, both in popular culture and within the field of organizational psychology. Unlike traditional measures of intelligence quotient (IQ), which primarily focus on cognitive abilities, EQ encompasses the ability to understand, manage, and utilize one's own emotions, as well as recognize and influence the emotions of others.  Proponents of EQ argue that it is a crucial factor in personal and professional success, sometimes even more so than IQ.  They suggest that individuals with high EQ are better equipped to navigate complex social situations, build strong relationships, and cope with stress and adversity. Critics, however, raise concerns about the validity and measurability of EQ, questioning whether it is truly distinct from personality traits or simply a rebranding of existing social skills.  Despite these debates, research continues to explore the multifaceted nature of emotional intelligence and its impact on various aspects of human life.
    """
    deck_name_to_use = "IELTS Cambridge - Web App Test" # Example deck name for testing

    label_for_test_cards = "Command Line Test Label" # Example label for command-line testing

    if process_ielts_passage_and_create_anki_cards(example_passage, deck_name=deck_name_to_use, card_label=label_for_test_cards): # Pass card_label here in test call
        print("\nExample passage processed and Anki cards imported successfully (using main.py directly)!")
    else:
        print("\nExample passage processing or Anki card import failed (using main.py directly). Check error messages above.")