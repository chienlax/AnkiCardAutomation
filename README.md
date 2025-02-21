# IELTS Anki Card Generator - Comprehensive Documentation

## 🎉 Supercharge Your IELTS Vocabulary Learning with AI-Powered Anki Cards! 🎉

### Effortlessly Create Anki Flashcards from IELTS Reading Passages Using Google Gemini AI

This application is your personal assistant for turning challenging IELTS reading passages into effective Anki flashcards. Forget manual vocabulary extraction and card creation!  The **IELTS Anki Card Generator** automates the entire process, allowing you to focus on learning and mastering essential IELTS vocabulary.

By simply pasting in any IELTS reading passage, this tool leverages the power of the **Google Gemini AI API** to:

*   **Intelligently Analyze Text:**  Understand the context and identify key vocabulary within your IELTS reading material.
*   **Extract Advanced Vocabulary & Phrasing:** Pinpoint words and phrases that are most relevant and beneficial for IELTS preparation, focusing on advanced and idiomatic language.
*   **Generate Rich Anki Cards:**  Create flashcards packed with valuable information, going far beyond simple word-definition pairs.

**Spend less time creating cards and more time learning!**

## Key Features - Unlock Your IELTS Vocabulary Potential

*   **🔥 AI-Powered Vocabulary Analysis with Google Gemini:**
    *   Utilizes the cutting-edge **Google Gemini Pro model** to deeply analyze IELTS reading passages.
    *   Intelligently identifies **advanced vocabulary words and good phrasing** that are highly relevant for IELTS test preparation.
    *   Saves you countless hours of manual vocabulary extraction and selection.

*   **📚 IELTS-Focused Vocabulary & Phrasing Selection:**
    *   Specifically tuned to recognize vocabulary and idiomatic expressions that are **appropriate for the advanced level required in the IELTS exam.**
    *   Goes beyond basic definitions to capture the nuances of language used in authentic IELTS reading materials.

*   **📝 Comprehensive & Feature-Rich Anki Cards:**
    *   **Front of Card: Word or Phrase** - Clearly presents the target vocabulary item.
    *   **Back of Card (HTML Formatted for Clarity):**
        *   **🔊 Pronunciation (US & UK):** Includes both US and UK pronunciations (when available) to improve listening and speaking skills, formatted for easy readability.
        *   **🏷️ Word Form (Part of Speech):**  Identifies the grammatical form (e.g., adjective, verb, noun, phrase) to enhance understanding of usage.
        *   **👨‍👩‍👧‍👦 Word Family:** Expands your vocabulary by providing related word forms (noun, verb, adjective, adverb) and their meanings (if different from the main word), building a richer vocabulary network.
        *   **🇬🇧 English Meaning:** Provides a concise and clear definition in English, suitable for IELTS learners.
        *   **🇻🇳 Vietnamese Meaning:** Offers an accurate and concise translation in Vietnamese for native Vietnamese speakers.
        *   **✍️ Example Sentence:** Presents a natural and contextual example sentence in English to demonstrate proper usage and understanding.

*   **🗂️ Direct Anki Import via AnkiConnect:**
    *   Seamlessly integrates with your Anki Desktop application using the **AnkiConnect add-on**.
    *   Imports generated flashcards directly into your Anki collection with just a few clicks in the web app.
    *   Eliminates manual exporting and importing of Anki card files.

*   **🏷️ Labeling for Effective Anki Organization:**
    *   **Choose Existing Labels:** Select from a dropdown list of labels already present in your Anki collection for consistent organization.
    *   **Create New Labels:**  Easily create new labels directly from the web app to categorize your IELTS vocabulary cards (e.g., by Cambridge book, passage topic, or word type).
    *   Improves card discoverability and targeted study within Anki.

*   **🌐 User-Friendly Web Interface:**
    *   Accessible through any web browser on your local machine.
    *   Clean and intuitive design for easy pasting of IELTS passages and card generation.
    *   Clear feedback messages to guide you through the card creation and import process.

*   **📦 Standalone Executable for Windows (Optional):**
    *   Provides instructions to build a `.exe` application using PyInstaller, allowing you to run the tool as a convenient desktop application on Windows without needing to run Python scripts directly.

## Installation - Get Started in Minutes

1.  **✅ Prerequisites - Before You Begin:**

    *   **Python 3.10+:** Ensure you have **Python 3.10 or a later version** installed on your computer. You can download the latest version from the official [Python website](https://www.python.org/downloads/).
    *   **Anki Desktop Application:** You must have the **Anki Desktop flashcard application** installed. Download it for free from the [Anki website](https://apps.ankiweb.net/).  This tool imports cards directly into Anki Desktop.
    *   **AnkiConnect Add-on:**  The **AnkiConnect add-on is essential** for this tool to communicate with Anki. Install it directly within Anki Desktop:
        1.  Open Anki Desktop.
        2.  Go to **Tools -> Add-ons -> Browse & Install...**
        3.  Enter the code `2055492159` and click **"OK"**.
        4.  Restart Anki to enable the add-on.
    *   **Google Gemini API Key:**  You will need a **Google Gemini API key** to access the Google Gemini AI model. Follow these steps to obtain one:
        1.  Go to [Google AI Studio](https://makersuite.google.com/).
        2.  Sign in with your Google account.
        3.  Create a new project if you don't have one already.
        4.  Navigate to **"Get API key"** or find the API key section in your project settings.
        5.  Copy and securely store your Gemini API key.

2.  **⬇️ Clone or Download the IELTS Anki Card Generator:**

    *   **Using Git (Recommended - If you have Git installed):**
        ```bash
        git clone [https://github.com/chienlax/AnkiCardAutomation]
        cd IELTS-Anki-Card-Generator # Or the name of the cloned directory
        ```
    *   **Download as ZIP File (If you don't use Git):**
        *   [Download ZIP Archive - Link to ZIP download here, e.g., GitHub Releases page, if applicable]
        *   Download the project as a ZIP file from the provided link.
        *   Extract the ZIP archive to your desired location on your computer (e.g., your Documents folder).
        *   Navigate to the extracted folder `AnkiCardAutomation` (or the name of the extracted folder).

3.  **<0xF0><0x9F><0xA7><0xBB> Set Up a Python Virtual Environment (Highly Recommended):**
    *   Using a virtual environment keeps your project dependencies isolated and prevents conflicts with other Python projects.
        ```bash
        python -m venv venv_ielts_anki_cards  # Creates a virtual environment folder named 'venv_ielts_anki_cards' (you can choose a different name)
        # Activate the virtual environment:
        # On Windows (Command Prompt or PowerShell):
        venv_ielts_anki_cards\Scripts\activate
        # On macOS/Linux (Bash or Zsh):
        source venv_ielts_anki_cards/bin/activate
        ```
        **(Important:** Make sure the virtual environment is activated before proceeding to the next steps. You'll know it's active when you see the environment name `(venv_ielts_anki_cards)` or similar in your terminal prompt.)

4.  **📦 Install Python Dependencies - All at Once or Individually:**

    *   **Recommended - Install all dependencies from `requirements.txt`:**  This is the easiest and recommended method.
        ```bash
        pip install -r requirements.txt
        ```
        **(Note:** This command will install all the necessary Python libraries listed in the `requirements.txt` file, which is included in the project repository.)

    *   **Alternatively - Install Core Libraries Individually:** If you prefer to install libraries one by one, use these commands:
        ```bash
        pip install flask google-generativeai requests anki
        ```

5.  **🔑 Set Your Gemini API Key as an Environment Variable:**
    *   The application needs your Google Gemini API key to access the Gemini AI service.  You must set it as an environment variable named `GOOGLE_API_KEY`.
        *   **On macOS or Linux:**
            1.  Open your shell configuration file (e.g., `.bashrc`, `.zshrc`, `.bash_profile`) using a text editor (like TextEdit, Nano, Vim, or VS Code). This file is usually located in your home directory (`~`).
            2.  Add the following line to the end of the file, **replacing `YOUR_API_KEY` with your actual Gemini API key** that you obtained from Google AI Studio:
                ```bash
                export GOOGLE_API_KEY="YOUR_API_KEY"
                ```
            3.  Save the file.
            4.  Apply the changes to your current terminal session by running:
                ```bash
                source ~/.bashrc  # If you edited .bashrc
                # OR
                source ~/.zshrc  # If you edited .zshrc
                # OR
                source ~/.bash_profile # If you edited .bash_profile
                ```
                (Use the command corresponding to the file you edited).
        *   **On Windows:**
            1.  Open the **"System Properties"** window: Search for "environment variables" in the Windows Start Menu and select "Edit the system environment variables".
            2.  Click the **"Environment Variables..."** button.
            3.  In the "System variables" section (or "User variables" if you only want it for your user), click **"New..."**.
            4.  In the "New System Variable" (or "New User Variable") dialog:
                *   **Variable name:** Enter `GOOGLE_API_KEY`
                *   **Variable value:** Enter your actual Gemini API key that you copied from Google AI Studio.
            5.  Click **"OK"** on all dialog boxes to save the changes.
            6.  **Restart your terminal or command prompt** for the environment variable to take effect.

## 🚀 Running the IELTS Anki Card Generator Web Application

1.  **Ensure Anki Desktop is Running:**  Make sure your Anki Desktop application is open and running in the background with the **AnkiConnect add-on enabled**.
2.  **Activate Your Virtual Environment:** If you created a virtual environment during installation, activate it now.
3.  **Navigate to the Project Directory:** Open your terminal or command prompt and navigate to the `AnkiCardAutomation` directory where you cloned or extracted the project files.
4.  **Start the Web Application:** Run the Flask web application by executing the following command:
    ```bash
    python web_ui.py
    ```
    You should see a message in the terminal indicating that the Flask development server is running (e.g., `* Running on http://127.0.0.1:5000/`).
5.  **Open the Web App in Your Browser:** Open your web browser (Chrome, Firefox, Safari, Edge, etc.) and go to the following address:
    ```
    http://127.0.0.1:5000/
    ```
    You should see the "IELTS Anki Card Generator" web interface in your browser.
6.  **Generate Anki Cards - Step-by-Step Guide:**
    *   **(1) Paste IELTS Reading Passage Text:** In the web app, locate the "IELTS Reading Passage Text" textarea. Copy the text content of an IELTS reading passage from a document, webpage, or PDF and paste it into this textarea.
    *   **(2) Optional: Set Anki Deck Name:** If you want to import the generated cards into a specific Anki deck (other than the default "IELTS Cambridge"), enter your desired deck name in the "Anki Deck Name" input field. If you leave it blank, cards will be imported into the "IELTS Cambridge" deck.
    *   **(3) Choose a Label for Your Cards:**
        *   **Select Existing Label:** Click on the "Choose Anki Label" dropdown menu. A list of labels already present in your Anki collection will be displayed. Select an appropriate label from the list to tag your new cards.
        *   **Create a New Label:** If you want to use a new label, select the "New label" option from the dropdown. A "New Label Name" text input field will appear. Enter the name for your new label in this field.
    *   **(4) Click "Generate Anki Cards":** Once you have pasted the passage text and selected or created a label (and optionally set a deck name), click the "Generate Anki Cards" button.
    *   **(5) Wait for Success Message:**  Wait for the application to process the passage and import the cards. Upon successful completion, you should see a **green success message** displayed on the webpage: "Successfully processed passage and imported Anki cards into deck '[Your Deck Name]' with label '[Your Label Name]'!".  Check the terminal for detailed output and debugging information if needed.
    *   **(6) Review Your Cards in Anki Desktop:** Open your Anki Desktop application.  Go to the Anki deck you specified (or "IELTS Cambridge" if you used the default). You should now find the newly generated IELTS vocabulary flashcards in that deck, tagged with the label you selected.

7.  **Stopping the Web Application:** When you are finished using the web application, simply press `Ctrl+C` (Control + C) in the terminal window where you are running `python web_ui.py`. This will gracefully shut down the Flask development server.

## 📦 Building a Standalone Executable for Windows (.exe)

For users who prefer to run the IELTS Anki Card Generator as a standalone Windows application (without needing to run Python scripts directly), you can build an executable (`.exe`) file using PyInstaller.

1.  **Install PyInstaller:** If you haven't already, install PyInstaller in your Python environment:
    ```bash
    pip install pyinstaller
    ```
2.  **Run PyInstaller to Create the `.exe`:** Navigate to your `AnkiCardAutomation` directory in the terminal and execute the following command:
    ```bash
    pyinstaller web_ui.spec
    ```
    **(Note:** Make sure you have the `web_ui.spec` file in your project root directory. If you don't have it yet, generate it first by running: `pyi-makespec --onefile web_ui.py`)
3.  **Locate the Executable File:** After PyInstaller completes the build process (which may take a few minutes), the standalone executable file named `web_ui.exe` will be located in the `dist` folder within your `AnkiCardAutomation` directory.
4.  **Run the `.exe` Application:**  Simply double-click the `web_ui.exe` file in the `dist` folder to launch the IELTS Anki Card Generator as a desktop application. It should automatically open your default web browser and display the web interface.
5.  **Stopping the `.exe` Application:** To stop the standalone application, close the terminal window that might appear running in the background alongside the web app. Alternatively, you can use the Task Manager (Ctrl+Shift+Esc on Windows) to find and end the `web_ui.exe` process if necessary.

## 💡 Usage Tips for Effective Vocabulary Learning

*   **Focus on High-Quality IELTS Passages:** Use authentic IELTS reading passages from Cambridge IELTS books or reputable IELTS practice websites to ensure the vocabulary is relevant and test-like.
*   **Regular Card Review in Anki:** The key to vocabulary learning with Anki is consistent review. Schedule regular review sessions in Anki Desktop to reinforce your learning and move words to long-term memory.
*   **Customize Cards in Anki:** Feel free to edit and enhance the generated Anki cards directly in Anki Desktop. You can add personal notes, context, images, audio, or further refine the definitions and example sentences to suit your learning style.
*   **Utilize Anki's Features:** Explore Anki's powerful features for spaced repetition, card scheduling, different card types, and study statistics to optimize your vocabulary learning process.
*   **Labeling Strategy:** Develop a consistent labeling strategy to organize your IELTS vocabulary cards effectively. Consider labeling by:
    *   **Cambridge IELTS Book Number:** (e.g., "Cambridge 18", "Cam17", etc.)
    *   **Passage Topic:** (e.g., "Science", "History", "Technology")
    *   **Word Type/Theme:** (e.g., "Advanced Verbs", "Idioms", "Academic Vocabulary")
    *   Combining labels can provide even finer-grained organization (e.g., "Cam18 - Passage 1 - Science").

## ⚠️ Troubleshooting - Common Issues and Solutions

*   **AnkiConnect Errors - "Could not connect to AnkiConnect...", etc.:**
    *   **Verify Anki Desktop is Running:** Ensure that your Anki Desktop application is open and running in the background *before* you use the IELTS Anki Card Generator web app or `.exe`.
    *   **Check AnkiConnect Add-on Enabled:**  Double-check that the AnkiConnect add-on is installed and enabled in Anki Desktop (Tools -> Add-ons). Restart Anki if you just installed or enabled it.
    *   **AnkiConnect Configuration (Usually Default is Fine):** In most cases, the default AnkiConnect settings work without modification. However, if you have changed AnkiConnect settings, ensure they are not preventing connections from `http://localhost:8765`.
    *   **Firewall or Security Software:**  In rare cases, firewall or security software on your computer might be blocking connections to `http://localhost:8765`.  Temporarily disable your firewall or security software (if you are comfortable doing so and understand the risks) to test if it's the cause. If it is, you may need to configure an exception for AnkiConnect or your web app.

*   **Gemini API Errors - "GOOGLE_API_KEY environment variable not set", API Key Invalid, Quota Exceeded:**
    *   **Environment Variable Not Set:**  Carefully re-read the "Installation" section and double-check that you have correctly set the `GOOGLE_API_KEY` environment variable in your operating system (either user or system variables). Ensure there are no typos in the variable name or API key value. Restart your terminal or command prompt after setting environment variables for them to take effect.
    *   **Invalid API Key:** Verify that the Gemini API key you are using is actually valid and has not expired or been revoked in your Google AI Studio project. Copy and paste the key directly from Google AI Studio to avoid typos.
    *   **API Quota Limits:**  Google Gemini API (like many AI services) has usage quotas and limits. If you are processing a very large number of passages in a short period, you might be hitting rate limits. Try reducing the frequency of your requests. Check your API usage and quota limits in your Google AI Studio project. Consider upgrading your API quota or exploring pricing if you need to process very large volumes of text.

*   **PyInstaller Build Errors - "multiple Qt bindings packages" or similar:**
    *   **Qt Bindings Conflict:** If you encounter errors during PyInstaller build mentioning "multiple Qt bindings packages" or PyQt, this usually indicates a conflict with PyQt5 and PyQt6 libraries in your Python environment. Refer back to the detailed troubleshooting steps discussed in the previous chat messages to resolve PyQt conflicts. This typically involves uninstalling extraneous PyQt packages or excluding them in the `web_ui.spec` file.

*   **Web Application "Internal Server Error" After Building `.exe`:**
    *   **Run `.exe` from Command Line for Traceback:** If you encounter a generic "Internal Server Error" when running the `.exe` application, **do not just double-click the `.exe`.** Instead, open a command prompt, navigate to the `dist` folder, and run `web_ui.exe` from the command line. This will show you detailed traceback error messages in the terminal output, which are essential for diagnosing the problem.
    *   **Template Not Found (`jinja2.exceptions.TemplateNotFound: index.html`):** This error means the `templates` folder and `index.html` file were not correctly packaged into the `.exe`. Ensure you have added the `datas=[ ('templates', 'templates') ],` line to your `web_ui.spec` file as described in the documentation to include the templates folder during the PyInstaller build process.
    *   **ModuleNotFoundError (e.g., `ImportError: No module named '...'`):** If you see `ImportError` messages in the traceback when running the `.exe`, it means PyInstaller did not automatically include all necessary Python libraries in the `.exe`. Try adding the missing module name to the `hiddenimports` list in your `web_ui.spec` file.

*   **Cards Not Appearing in Anki After Import:**
    *   **Check Anki Deck Name:** Double-check that you are looking in the correct Anki deck in Anki Desktop – the deck name you specified in the web app (or "IELTS Cambridge" if you used the default).
    *   **Verify Label:** Look for the label you selected (or the default label if you didn't specify one) in the Anki browser. Ensure the imported cards are tagged with that label.
    *   **Anki Sync Issues:** If you are using AnkiWeb sync, sometimes there might be a delay in synchronization. Try manually syncing Anki Desktop to ensure the latest changes are reflected.

---

Thank u Gemini 2.0 Flash Thinking. I couldn't have done it without you.