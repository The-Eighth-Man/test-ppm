from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
    if(request.method == 'GET'):
        data = {"data": "Hello, World!"}
        return jsonify(message=data)

if __name__ == '__main__':
    app.run(debug=True)