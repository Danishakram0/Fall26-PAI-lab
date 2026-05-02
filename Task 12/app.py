from flask import Flask, request, render_template, session
import pandas as pd
import numpy as np
import re
import faiss
from sentence_transformers import SentenceTransformer

app = Flask(__name__)
app.secret_key = "admissions-bot-secret-2026"

df = pd.read_csv("admissionsqna.csv")
print(f"[INFO] Loaded {len(df)} QnA pairs.")


def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

df["Processed"] = df["Question"].apply(preprocess)


print("[INFO] Loading SentenceTransformer model...")
model = SentenceTransformer('all-MiniLM-L6-v2')

print("[INFO] Encoding questions...")
embeddings = model.encode(df["Processed"].tolist(), show_progress_bar=True)
embeddings = np.array(embeddings).astype('float32')


dimension = embeddings.shape[1]
faiss_index = faiss.IndexFlatL2(dimension)
faiss_index.add(embeddings)
print(f"[INFO] FAISS index built with {faiss_index.ntotal} vectors.")


SIMILARITY_THRESHOLD = 1.2 

def get_answer(user_query):
    """Return the best matching answer and the matched question."""
    processed = preprocess(user_query)
    query_vec = model.encode([processed]).astype('float32')
    distances, indices = faiss_index.search(query_vec, k=1)

    dist = distances[0][0]
    idx  = indices[0][0]

    if dist > SIMILARITY_THRESHOLD:
        return (
            "I'm sorry, I don't have information on that topic. "
            "Please contact the admissions office at admissions@university.edu.pk "
            "or call 0300-0000000.",
            None,
            dist
        )

    matched_question = df.iloc[idx]["Question"]
    answer           = df.iloc[idx]["Answer"]
    return answer, matched_question, dist

@app.route("/", methods=["GET", "POST"])
def home():
    if "chat" not in session:
        session["chat"] = []

    if request.method == "POST":
        user_msg = request.form.get("question", "").strip()
        if user_msg:
            bot_msg, matched_q, dist = get_answer(user_msg)

            chat = session["chat"]
            chat.append({
                "user": user_msg,
                "bot":  bot_msg,
                "matched": matched_q,
                "score": round(float(dist), 4)
            })
            session["chat"] = chat
            session.modified = True

    return render_template("index.html", chat=session["chat"])


@app.route("/clear", methods=["POST"])
def clear():
    session.pop("chat", None)
    return ("", 204)


if __name__ == "__main__":
    app.run(debug=True)
