from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os

# Load environment variables from a .env file (only in local dev)
load_dotenv()

# Create Flask app
app = Flask(__name__)
CORS(app, methods=["GET"])  # Allow CORS for all origins but restrict to GET requests

# Define the /products route
@app.route('/products', methods=['GET'])
def get_products():
    products = [
        {"id": 1, "name": "Dog Food", "price": 19.99},
        {"id": 2, "name": "Cat Food", "price": 34.99},
        {"id": 3, "name": "Bird Seeds", "price": 10.99},
    ]
    return jsonify(products)

# Entry point
if __name__ == '__main__':
    port = int(os.getenv("PORT", 3030))  # Default to port 3030
    app.run(host='0.0.0.0', port=port)
