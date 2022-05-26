from flask import Flask, jsonify, request
from model import model
from image_predictions import predict

app = Flask(__name__)


@app.route('/')
def home():
    return '<a href="http://127.0.0.1:5000/predict">Go to predictions page</a>'


@app.route('/predict', methods=['POST'])
def predictions():
    image = request.files.get('alphabets')

    predictions = predict(image, model)

    return jsonify({'data': predictions}), 200


if __name__ == '__main__':
    app.run(debug=True)
