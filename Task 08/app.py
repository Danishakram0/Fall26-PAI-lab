import requests
from flask import Flask, render_template

app = Flask(__name__)

API_KEY = "AIzaSyDkP7QBPTj3fZ-L23ICZCRzwpeQ0i4skNM"

@app.route('/')
def home():
    url = f"https://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey={API_KEY}"
    news_list = []
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            news_list = data.get('articles', [])
    except:
        pass
    return render_template('index.html', news_list=news_list)

if __name__ == '__main__':
    app.run(debug=True)
