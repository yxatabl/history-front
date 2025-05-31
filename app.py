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
            with open("test1.md", "r") as file:
                md = file.read()
            with open("test2.md", "r") as file:
                md2 = file.read()
            with open("test3.md", "r") as file:
                md3 = file.read()
            with open("test4.md", "r") as file:
                md4 = file.read()
            with open("test5.md", "r") as file:
                md5 = file.read()
            events = [
                {
                    "id": 1,
                    "title": "Битва на тайпале",
                    "place": {
                        "id": 101,
                        "name": "Кексгольмский уезд, Финляндия",
                        "latitude": 61,
                        "longitude": 30.1
                    },
                    "markdown": md 
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
                    "markdown": md2 
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
                    "markdown": md3
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
                    "markdown": md4
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
                    "markdown": md5
                },
            ]
            
        return jsonify(events)
    except requests.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")