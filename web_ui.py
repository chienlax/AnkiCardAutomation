from flask import Flask, render_template, request, flash, redirect, url_for
from main import process_ielts_passage_and_create_anki_cards  # Import the orchestration function from main.py
from generate_anki_cards import get_tags # Import get_tags function
import webbrowser  # ADD THIS LINE: Import the webbrowser module
import threading  # ADD THIS LINE: Import the threading module

app = Flask(__name__)
app.secret_key = "ielts_anki_secret"  # Required for flash messages (you can change this to any random string)

@app.route("/", methods=["GET", "POST"])
def index():
    labels = get_tags() or [] # Fetch existing labels from Anki, default to empty list if fails
    if labels is None: # Handle error getting labels (e.g., AnkiConnect not working)
        labels = []
        flash("Could not retrieve Anki labels. AnkiConnect might not be working.", "warning")

    if request.method == "POST":
        ielts_passage_text = request.form.get("ielts_passage")
        deck_name = request.form.get("deck_name") or "IELTS Cambridge"
        label_choice = request.form.get("label_choice") # Get selected label choice from dropdown
        new_label = request.form.get("new_label") # Get new label text input

        if not ielts_passage_text:
            flash("Please enter or paste the IELTS reading passage text.", "error")
        else:
            selected_label = ""
            if label_choice == "new_label":
                selected_label = new_label.strip()
                if not selected_label:
                    flash("Please enter a new label name.", "error")
                    return render_template("index.html", labels=labels) # Re-render with labels, keep existing input
            else:
                selected_label = label_choice

            if selected_label: # Proceed only if we have a valid label
                if process_ielts_passage_and_create_anki_cards(ielts_passage_text, deck_name=deck_name, card_label=selected_label): # Pass label to processing function (modify main.py next)
                    flash(f"Successfully processed passage and imported Anki cards into deck '{deck_name}' with label '{selected_label}'!", "success")
                else:
                    flash("Passage processing or Anki card import failed. See console for details.", "error")

    return render_template("index.html", labels=labels) # Pass labels to template for GET requests as well

def open_browser(): # ADD THIS FUNCTION: Function to open browser
    webbrowser.open_new('http://127.0.0.1:5000/')

if __name__ == "__main__":
    threading.Timer(1, open_browser).start() # ADD THIS LINE: Open browser after 1 second delay
    app.run(debug=False) # Run the Flask app (debug=False for exe, important!)