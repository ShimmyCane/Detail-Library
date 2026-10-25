from flask import Flask, request, jsonify
from database import add_detail
from queries import get_all_details
import os

app = Flask(__name__)

@app.route('/api/details', methods=['GET'])
def list_details():
    return jsonify(get_all_details())

@app.route('/api/ingest', methods=['POST'])
def ingest():
    data = request.json
    # In a real scenario, we'd call an LLM here to generate tags/description
    # For now, we accept them from the request
    add_detail(
        data['filename'],
        data['project'],
        data['category'],
        data['tags'],
        data['description'],
        data['metadata']
    )
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(port=5000)

