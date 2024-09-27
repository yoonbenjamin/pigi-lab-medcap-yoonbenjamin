# server/app.py
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing (CORS) to allow interaction with the frontend

# Root route just to test the server is running
@app.route('/')
def index():
    return jsonify({"message": "Flask backend is running!"})

# Placeholder route for future file uploads
@app.route('/upload', methods=['POST'])
def upload_file():
    # This is where you will implement the file upload logic
    return jsonify({"message": "File upload endpoint is ready!"})

# Placeholder route for future database file retrieval
@app.route('/files', methods=['GET'])
def retrieve_files():
    # This is where you will implement file retrieval from a database
    return jsonify({"files": []})

# Start the server
if __name__ == '__main__':
    app.run(debug=True, port=5000)
