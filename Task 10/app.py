from flask import Flask, render_template, request, jsonify
from chatbot_logic import get_bot_response

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def chat():
    user_message = request.json.get("message")
    if not user_message:
        return jsonify({"response": "I didn't catch that. Could you repeat?"})
    
    # Logic file se response lana
    bot_reply = get_bot_response(user_message.lower())
    return jsonify({"response": bot_reply})

if __name__ == '__main__':
    app.run(debug=True)
