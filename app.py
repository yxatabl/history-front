from flask import Flask, render_template, jsonify
import requests  # For API calls (install with pip install requests)

app = Flask(__name__)

# Mock API endpoint - replace with your actual API URL
API_URL = "https://localhost:8080/api/events/test"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/events')
def get_events():
    try:
        # Fetch events from the external API
        events = None
        
        # Mock data in case API is not available (for testing)
        if not events:
            mds = []
            for i in range(7):
                with open(f"test{i+1}.md", "r") as file:
                    mds.append(file.read())
            events = [
                {
                    "id": 1,
                    "title": "Битва на Тайпале",
                    "place": {
                        "id": 101,
                        "name": "Кексгольмский уезд, Финляндия",
                        "latitude": 61,
                        "longitude": 30.1
                    },
                    "markdown": mds[0]
                },
                {
                    "id": 2,
                    "title": "Битва при Колле",
                    "place": {
                        "id": 102,
                        "name": "озеро Колласъярви",
                        "latitude": 61.77,
                        "longitude": 32.16
                    },
                    "markdown": mds[1]
                },
                {
                    "id": 3,
                    "title": "Прорыв линии Маннергейма",
                    "place": {
                        "id": 103,
                        "name": "Карельский перешеек",
                        "latitude": 60.42,
                        "longitude": 29.99
                    },
                    "markdown": mds[2]
                },
                {
                    "id": 4,
                    "title": "Битва при Толваярви",
                    "place": {
                        "id": 104,
                        "name": "Озеро Толвоярви",
                        "latitude": 62.28,
                        "longitude": 31.48
                    },
                    "markdown": mds[3]
                },
                {
                    "id": 5,
                    "title": "Майнильский инцидент",
                    "place": {
                        "id": 105,
                        "name": "деревня Майнило",
                        "latitude": 60.26,
                        "longitude": 29.84
                    },
                    "markdown": mds[4]
                },
                {
                    "id": 6,
                    "title": "Битва на Раатской дороге",
                    "place": {
                        "id": 106,
                        "name": "Суомосалми",
                        "latitude": 64.88,
                        "longitude": 28.91
                    },
                    "markdown": mds[5]
                },
                {
                    "id": 7,
                    "title": "Битва при Салле",
                    "place": {
                        "id": 107,
                        "name": "волость Салла",
                        "latitude": 66.83,
                        "longitude": 28.67
                    },
                    "markdown": mds[6]
                },
                {
                    "id": 8,
                    "title": "Битва при Суомуссалми",
                    "place": {
                        "id": 108,
                        "name": "Суомуссалми",
                        "latitude": 64.88,
                        "longitude": 28.91
                    },
                    "markdown": mds[7]
                },
                {
                    "id": 9,
                    "title": "Бои в Петсамо",
                    "place": {
                        "id": 109,
                        "name": "Петсамо (сейчас Печенга)",
                        "latitude": 69.55,
                        "longitude": 31.20
                    },
                    "markdown": mds[8]
                },
            ]
            
        return jsonify(events)
    except requests.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")