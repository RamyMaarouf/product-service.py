from flask import Flask, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv

# Load environment variables from a .env file (for local development)
load_dotenv()

# Create a Flask app instance
app = Flask(__name__)

# Enable CORS for all origins (only allowing GET requests)
CORS(app, resources={r"/products": {"origins": "*"}}, methods=["GET"])

# Sample products data (simulating a JSON array of product objects)
PRODUCTS = [
    {"id": 1, "name": "Dog Food", "price": 19.99},
    {"id": 2, "name": "Cat Food", "price": 34.99},
    {"id": 3, "name": "Bird Seeds", "price": 10.99},
]

# Define the `/products` route
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(PRODUCTS)

# Entry point
if __name__ == '__main__':
    # Get port from environment variable or default to 3030
    port = int(os.getenv("PORT", 3030))
    app.run(host='0.0.0.0', port=port)
