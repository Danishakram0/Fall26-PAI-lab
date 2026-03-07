from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

API_KEY = "c38c31e59856f55d8df120f803248580"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


@app.route("/")
def home():
    return jsonify({
        "message": "Weather API is running"
    })


@app.route("/weather", methods=["GET"])
def get_weather():

    city = request.args.get("city")

    if not city:
        return jsonify({"error": "City is required"}), 400

    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)
    data = response.json()

    if data["cod"] != 200:
        return jsonify({"error": "City not found"}), 404

    weather_data = {
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "weather": data["weather"][0]["description"],
        "wind_speed": data["wind"]["speed"]
    }

    return jsonify(weather_data)


if __name__ == "__main__":
    app.run(debug=True)