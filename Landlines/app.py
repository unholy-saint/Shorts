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
    return jsonify({"data": contacts})


@app.route('/addData', methods=['POST'])
def addData():
    contacts.append({
        "Name": "Mukesh Ambani",
        "Contact": "1029384756",
        "id": 3
    })
    return jsonify({"data": contacts})

@app.route('/deleteData', methods=['DELETE'])
def delete():
    contacts.pop(1)

    return jsonify({'data':contacts})

if __name__ == "__main__":
    app.run(debug=True)
