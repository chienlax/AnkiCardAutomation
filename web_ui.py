from flask import Flask, render_template, request, flash, redirect, url_for
from main import process_ielts_passage_and_create_anki_cards  # Import the orchestration function from main.py

app = Flask(__name__)
app.secret_key = "ielts_anki_secret"  # Required for flash messages (you can change this to any random string)

@app.route("/", methods=["GET", "POST"])
def index():
    message = None
    if request.method == "POST":
        ielts_passage_text = request.form.get("ielts_passage")
        deck_name = request.form.get("deck_name") or "IELTS Cambridge" # Get deck name from form or use default

        if not ielts_passage_text:
            flash("Please enter or paste the IELTS reading passage text.", "error") # Flash error message
        else:
            if process_ielts_passage_and_create_anki_cards(ielts_passage_text, deck_name=deck_name):
                flash(f"Successfully processed passage and imported Anki cards into deck '{deck_name}'!", "success") # Flash success message
            else:
                flash("Passage processing or Anki card import failed. See console for details.", "error") # Flash general error message

    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(debug=True) # Run the Flask app in debug mode (for development)