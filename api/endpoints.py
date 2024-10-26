from ai import ask_ai_for_advice
from help_functions import push_data_to_db, get_team_data_from_db
from generate_wykres import generate_wykres_sleep_time, generate_wykres_stress_time
from generate_pdf import gen_pdf
from flask import Flask, request, jsonify, send_file
import os

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
    
    push_data_to_db(input_string)
    response="added data to db"
    
    return jsonify(response), 200


@app.route('/generate_raport', methods=['POST'])
def generate_raport():
    data = request.get_json()
    id = data['id_teamu']
    
    wykres1_path="api/data/wykres1.png"
    wykres2_path="api/data/wykres2.png"
    pdf_path="api/data/raport.pdf"
    
    dni,dlugosc_spania, dlugosc_dobrego_spania, dlugosc_stresu=get_team_data_from_db(id)
    generate_wykres_sleep_time(dni, dlugosc_spania, dlugosc_dobrego_spania, wykres1_path)
    generate_wykres_stress_time(dni, dlugosc_stresu, wykres2_path)
    
    gen_pdf(pdf_path, wykres1_path, wykres2_path)
        
    if not os.path.exists(pdf_path):
        return jsonify({"error": "Failed to generate report"}), 500
    
    return send_file("data\\raport.pdf", as_attachment=True), 200


if __name__ == '__main__':
    app.run(debug=True)
