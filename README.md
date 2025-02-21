# IELTS Anki Card Generator

## Description

This application is a local web app designed to help you create Anki flashcards for IELTS vocabulary learning from IELTS reading passages.  It leverages the Google Gemini AI API to analyze IELTS reading passages, identify advanced vocabulary and good phrasing, and then automatically generate Anki cards with English and Vietnamese meanings, example sentences, pronunciation, word form, and word family information. The cards are then imported directly into your Anki flashcard application using AnkiConnect.

## Features

*   **Automated Vocabulary Analysis:** Uses Google Gemini AI to analyze IELTS reading passages.
*   **Advanced Vocabulary & Phrasing Identification:**  Identifies advanced words and good phrases suitable for IELTS level.
*   **Detailed Card Information:** Generates Anki cards with:
    *   Word/Phrase (Front of card)
    *   Pronunciation (US and UK)
    *   Word Form (e.g., adj, verb, phrase)
    *   Word Family (noun, verb, adjective, adverb forms with meanings)
    *   English Meaning
    *   Vietnamese Meaning
    *   Example Sentence (English)
*   **HTML Formatted Back of Card:**  Clear and readable card back with HTML formatting for line breaks and field separation.
*   **Direct Anki Import:** Imports cards directly into your Anki Desktop application using AnkiConnect.
*   **Label Selection:** Allows you to choose an existing Anki label or create a new label for the imported cards.
*   **Simple Web User Interface:** Easy-to-use web interface to paste IELTS passages and generate cards.
*   **Standalone Executable (Windows):**  Option to build a `.exe` application for easy execution on Windows.

## Installation

1.  **Prerequisites:**
    *   **Python 3.10 or higher** installed on your system.
    *   **Anki Desktop application** installed.
    *   **AnkiConnect add-on** installed and enabled in Anki Desktop (get it from AnkiWeb Add-ons).
    *   **Google Gemini API Key:** You need a Google Gemini API key. You can obtain one from [Google AI Studio](https://makersuite.google.com/).
2.  **Clone or Download the Repository:**
    *   If you are using Git, clone this repository to your local machine:
        ```bash
        git clone [repository URL]
        cd AnkiCardAutomation
        ```
    *   Alternatively, download the project as a ZIP file and extract it to your desired location.
3.  **Set up a Python Virtual Environment (Recommended):**
    ```bash
    python -m venv venv_anki_cards
    # Activate the virtual environment:
    # On Windows:
    venv_anki_cards\Scripts\activate
    # On macOS/Linux:
    source venv_anki_cards/bin/activate
    ```
4.  **Install Python Libraries:**  Install the required Python libraries using pip:
    ```bash
    pip install -r requirements.txt
    ```
    (Make sure you create a `requirements.txt` file listing dependencies if you want to be extra thorough, or just install them directly as listed below)
    Alternatively, install them individually:
    ```bash
    pip install flask google-generativeai requests anki
    ```
5.  **Set Gemini API Key as Environment Variable:**
    *   Set your Google Gemini API key as an environment variable named `GOOGLE_API_KEY`.
        *   **On macOS/Linux:** Add `export GOOGLE_API_KEY="YOUR_API_KEY"` to your `.bashrc`, `.zshrc`, or `.bash_profile` file, and then run `source ~/.bashrc` (or your shell config file).
        *   **On Windows:** Set a system or user environment variable named `GOOGLE_API_KEY` with your API key as the value (using System Properties -> Environment Variables).

## Running the Web Application (for development or direct Python execution)

1.  **Ensure Anki Desktop is running** with the AnkiConnect add-on enabled.
2.  **Navigate to the `AnkiCardAutomation` directory** in your terminal.
3.  **Run the web application:**
    ```bash
    python web_ui.py
    ```
4.  **Open your web browser** and go to `http://127.0.0.1:5000/`.
5.  **Use the web interface:**
    *   Paste your IELTS reading passage text into the "IELTS Reading Passage Text" area.
    *   Optionally, enter a deck name in the "Anki Deck Name" field (default is "IELTS Cambridge").
    *   Choose an existing Anki label from the dropdown or select "New label" and enter a new label name.
    *   Click "Generate Anki Cards".
6.  **Check for success message** on the webpage and in the terminal.
7.  **Open Anki Desktop** to see the newly imported cards in your specified deck.
8.  **To stop the web application:** Press `Ctrl+C` in the terminal where `web_ui.py` is running.

## Building a Standalone Executable (.exe for Windows)

1.  **Install PyInstaller:**
    ```bash
    pip install pyinstaller
    ```
2.  **Run PyInstaller to create the `.exe` file:**
    ```bash
    pyinstaller web_ui.spec
    ```
    (Make sure you have the `web_ui.spec` file in your project root directory. If you don't have it, run `pyi-makespec --onefile web_ui.py` to generate it first.)
3.  **Find the Executable:** The `.exe` file will be located in the `dist` folder within your `AnkiCardAutomation` directory.
4.  **Run the `.exe` file:** Double-click `web_ui.exe`. It will automatically open your web browser and launch the application.
5.  **To stop the `.exe` application:** Close the terminal window that might appear alongside the web app, or use Task Manager to end the `web_ui.exe` process if necessary.

## Usage Instructions

1.  **Open the IELTS Anki Card Generator web app** in your browser (either by running `web_ui.py` or the `web_ui.exe`).
2.  **Copy and paste the text content of an IELTS reading passage** into the "IELTS Reading Passage Text" textarea.
3.  **Optionally change the Anki Deck Name** if you want to import cards into a deck other than "IELTS Cambridge".
4.  **Choose a Label:** Select an existing Anki label from the "Choose Anki Label" dropdown, or choose "New label" and enter a new label name in the "New Label Name" field. Labels help you organize your cards in Anki.
5.  **Click "Generate Anki Cards".**
6.  **Wait for the "success" message** to appear on the webpage. This indicates that the passage has been processed and cards have been imported into Anki.
7.  **Open Anki Desktop** and check your specified deck ("IELTS Cambridge" by default) to see the newly created flashcards.

## Troubleshooting

*   **AnkiConnect Errors:**
    *   Ensure Anki Desktop is running and the AnkiConnect add-on is installed and enabled.
    *   Check if AnkiConnect is properly configured (usually, default settings work).
*   **Gemini API Errors:**
    *   Verify that you have set the `GOOGLE_API_KEY` environment variable correctly.
    *   Check if your Gemini API key is valid and active in your Google AI Studio project.
    *   If you encounter rate limit errors, you might need to reduce the frequency of usage or explore Gemini API usage limits.
*   **PyInstaller Build Errors:**
    *   If you encounter PyQt-related errors during PyInstaller build (like "multiple Qt bindings"), try uninstalling PyQt6 (if you don't need it) or excluding PyQt6 in the `web_ui.spec` file as described in the previous troubleshooting discussions.
    *   Ensure you are running PyInstaller in the correct Python environment where all your project dependencies are installed.

This is my first project buidling a web app with Python, well i should have done it earlier but better late than never. Thank u Gemini 2.0 Flash Thinking, i could not have done it without you. Remember to take your API key from Google AI Studio and set it as an environment variable.