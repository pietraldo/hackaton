from flask import Flask, request, jsonify
from ai import ask_ai_for_advice

app = Flask(__name__)

@app.route('/get_ai_recomendation', methods=['POST'])
def get_ai_recomendation():
    data = request.get_json()  # Get JSON data from the request
    if not data or 'health_problems' not in data:
        return jsonify({'error': 'No input string provided'}), 400

    input_string = data['health_problems']
    response=ask_ai_for_advice(input_string)
    
    return jsonify(response), 200


@app.route('/save_data', methods=['POST'])
def save_data():
    data = request.get_json()  
    if not data or 'health_data' not in data:
        return jsonify({'error': 'No input string provided'}), 400

    input_string = data['health_data']
    response="added data to db"
    
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)
