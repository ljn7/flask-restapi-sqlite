from flask import Flask, request, Response, jsonify
from start import *

app = Flask(__name__)

@app.route('/user', methods=['GET'])
def test():
    return 'Hello, World!'

if __name__ == "__main__":
    app.run(port=SERVER_PORT, debug=True)