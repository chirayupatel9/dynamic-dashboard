from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)


@app.route('/')
def hello():
    return jsonify({'message': 'Hello World!'})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
