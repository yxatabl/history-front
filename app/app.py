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
            with open("/home/vladimir/Documents/code/history/history-front/test1.md", "r") as file:
                md = file.read()
            with open("/home/vladimir/Documents/code/history/history-front/test2.md", "r") as file:
                md2 = file.read()
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
                
            ]
            
        return jsonify(events)
    except requests.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")