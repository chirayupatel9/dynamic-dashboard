from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_cors import CORS
import os


app = Flask(__name__)
CORS(app, origins=['http://localhost:3000', 'http://*:3000', 'http://127.0.0.1:3000', '*'])

version = os.getenv('version')  #
prefix = os.getenv('prefix')  #

UPLOAD_FOLDER = 'uploads/'


@app.route('/')
def hello():
    return jsonify({'message': 'Hello World!'})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
