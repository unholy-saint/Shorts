from flask import Flask, jsonify, request
from model import Predict

app = Flask(__name__)


@app.route('/')
def home():
    return 'Home'


@app.route('/predictions', methods=['POST'])
def predictions():
    img = request.files.get('digit')

    predict = Predict(img)

    return jsonify({'data': predict}), 200


if __name__ == '__main__':
    app.run(debug=True)
