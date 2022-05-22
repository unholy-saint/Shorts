from flask import Flask, jsonify

app = Flask(__name__)

contacts = [
    {
        "Name": "Mark Zuckerburg",
        "Contact": "1234567890",
        "id": 1
    },
    {
        "Name": "Jeff Bezoz",
        "Contact": "0987654321",
        "id": 2
    }
]


@app.route('/', methods=['GET'])
def showData():
    return '<h1>'+contacts+'<h1>'


@app.route('/addData', methods=['POST'])
def addData():
    contacts.append({
        "Name": "Mukesh Ambani",
        "Contact": "1029384756",
        "id": 3
    })
    return '<h1>' + jsonify({"data": contacts}) + '<h1>'
