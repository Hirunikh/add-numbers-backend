### Importing Libraries
```python
from flask import Flask, request, jsonify
from flask_cors import CORS
```
### Creating the Flask App
```
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
```
## Defining Routes and Functions
### Route for adding numbers through a POST request
```
@app.route('/add', methods=['POST'])
def add_numbers():
    """
    Handles a POST request to '/add'. Retrieves JSON data from the request,
    extracts 'num1' and 'num2', adds them, and returns the result as JSON.
    """
    # Extract JSON data from the request
    data = request.get_json()

    # Extract 'num1' and 'num2' from the JSON data
    num1 = data['num1']
    num2 = data['num2']

    # Perform addition and convert to float to handle decimal values
    result = float(num1) + float(num2)

    # Return the result as JSON
    return jsonify({'result': result})
```
### Route for a basic health check through a GET request
```
@app.route('/')
def health_check():
    """
    Handles a GET request to '/'. Returns a simple health check message.
    """
    return "<h2> add-numbers-backend running ... </h2>"
```
## Running the App
### Check if the script is being run directly
```
if __name__ == '__main__':
    # Start the Flask development server with debugging enabled
    app.run(debug=True)
```