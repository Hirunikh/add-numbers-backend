from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/add', methods=['POST'])
def add_numbers():
    try:
        data = request.get_json()
        number1 = float(data['number1'])
        number2 = float(data['number2'])
        result = {'result': number1 + number2}
        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)