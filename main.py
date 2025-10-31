from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    data = {"data": "Hello, World!"}
    return jsonify(message=data)

@app.route('/hello', methods=['GET'])
def hello():
    if request.method == 'GET':
        data = {"data": "Hello from /hello!"}
        return jsonify(message=data)

if __name__ == '__main__':
    app.run(debug=True)