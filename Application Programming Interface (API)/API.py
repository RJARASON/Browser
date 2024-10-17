from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return "MyAPIs"


@app.route('/languages', methods=['GET'])
def get_items():
    languages = [
        "Programming languages",

        {"id": 1, "language": "PHP"},
        {"id": 2, "language": "javascript"},
        {"id": 3, "language": "python"},
        {"id": 4, "language": "html"},
        {"id": 5, "language": "XML"},
        {"id": 6, "language": "C++"},
        {"id": 7, "language": "JSON"},
        {"id": 8, "language": "Objective C"},
        {"id": 9, "language": "Batch"},
        {"id": 10, "language": "Powershell"},
        {"id": 11, "language": "Binary"},
        {"id": 12, "language": "CSS"}
    ]
    return jsonify(languages)


@app.route('/IDEs', methods=['POST'])
def getIde():
    IDEs=[
        "Intergrated Development Environments",

        {"id": 1, "IDE":"Visual Studio Code"},
        {"id": 2, "IDE":"Sublime text"},
        {"id": 3, "IDE":"PyCharm"},
        {"id": 4, "IDE":"Ecplise"},
        {"id": 5, "IDE":"IntelliJ IDEA"},
        {"id": 6, "IDE":"NetBeans"},
        {"id": 7, "IDE":"Atom"},
        {"id": 8, "IDE":"Xcode"},
        {"id": 9, "IDE":"Andriod Studio"},
        {"id": 10, "IDE":"RubyMine"}
    ]
    return jsonify(IDEs)


@app.route('/IDE')
def create_item():
    newdata={"id":11, "IDE":"Pro Pixel"}
    datapost=requests.post(data=newdata,url="http://127.0.0.1:5000/IDE",json=newdata)
    return jsonify(datapost), 201


if __name__ == '__main__':
    app.run(debug=True)