from flask import Flask, request, Response, jsonify

app = Flask(__name__)

@app.route('/user', methods=['GET'])
def test():
    return 'Hello, World!'

if __name__ == "__main__":
    app.run(port=8080, debug=True)