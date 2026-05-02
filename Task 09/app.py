from flask import Flask, request, render_template, session
import nltk
import re

nltk.download('vader_lexicon', quiet=True)

from nltk.sentiment.vader import SentimentIntensityAnalyzer

app = Flask(__name__)
app.secret_key = "sentiment-nlp-lab-2024"


sia = SentimentIntensityAnalyzer()



def preprocess(text: str) -> str:
    """
    Light preprocessing suitable for VADER:
    - Strip leading/trailing whitespace
    - Collapse multiple spaces
    - Remove non-ASCII characters
    Note: VADER is designed for social-media text so we
    intentionally KEEP punctuation (!, ?) and casing because
    VADER uses them as sentiment signals.
    """
    text = text.strip()
    text = re.sub(r'[^\x00-\x7F]+', ' ', text)  
    text = re.sub(r' {2,}', ' ', text)       
    return text



def analyze(text: str) -> dict:
    """
    Run VADER and return a structured result dict.

    VADER compound score interpretation:
      >= 0.05  → Positive
      <= -0.05 → Negative
      else     → Neutral
    """
    cleaned = preprocess(text)
    scores  = sia.polarity_scores(cleaned)   

    compound = scores['compound']
    if compound >= 0.05:
        label = "Positive"
        emoji = "😊"
        color = "positive"
    elif compound <= -0.05:
        label = "Negative"
        emoji = "😠"
        color = "negative"
    else:
        label = "Neutral"
        emoji = "😐"
        color = "neutral"

    return {
        "original" : text,
        "cleaned"  : cleaned,
        "label"    : label,
        "emoji"    : emoji,
        "color"    : color,
        "compound" : round(compound, 4),
        "positive" : round(scores['pos']  * 100, 1),
        "negative" : round(scores['neg']  * 100, 1),
        "neutral"  : round(scores['neu']  * 100, 1),
    }



SAMPLES = [
    "I absolutely love this university! The teachers are amazing.",
    "This course is so boring and the assignments are terrible.",
    "The exam is scheduled for next Monday.",
    "The food in the cafeteria is surprisingly good today!",
    "I failed my test. Worst day ever.",
    "The library opens at 8 AM on weekdays.",
]



@app.route("/", methods=["GET", "POST"])
def home():
    if "history" not in session:
        session["history"] = []

    result = None

    if request.method == "POST":
        user_text = request.form.get("text", "").strip()
        if user_text:
            result = analyze(user_text)

           
            history = session["history"]
            history.insert(0, result)
            session["history"] = history[:20]   
            session.modified = True

    return render_template(
        "index.html",
        result=result,
        history=session["history"],
        samples=SAMPLES
    )


@app.route("/clear", methods=["POST"])
def clear():
    session.pop("history", None)
    return ("", 204)


if __name__ == "__main__":
    app.run(debug=True)
