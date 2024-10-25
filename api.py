from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/data', methods=['GET'])
def get_data():
    sample_data = {
        "heart_rate": 75,
        "steps": 1234,
        "sleep": {
            "duration": "7h 45m",
            "deep_sleep": "2h",
            "light_sleep": "4h",
            "rem_sleep": "1h 45m"
        },
        "timestamp": "2024-10-25T08:30:00Z"
    }
    print("Sending data:", sample_data)  # Check server logs for data output
    return jsonify(sample_data)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
