from flask import Flask, request, jsonify
from flask_cors import CORS  # Import the CORS module

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/add', methods=['POST'])
def add_numbers():
    data = request.get_json()
    num1 = data['num1']
    num2 = data['num2']
    result = float(num1) + float(num2)
    return jsonify({'result': result})

@app.route('/')
def health_check():
    return "<h2> add-numbers-backend running ... </h2>"

if __name__ == '__main__':
    app.run(debug=True)
