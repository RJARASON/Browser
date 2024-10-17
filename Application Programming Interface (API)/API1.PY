from flask import Flask,jsonify,request
import requests

app=Flask(__name__)

@app.route("/")
def home():
    return "API CREATE TEST"

@app.route("/index", methods=['GET'])
def index():
    languages=[
        {"Name":"Sarah","language":"English"},
        {"Name":"John","language":"French"},
        {"Name":"Nick","language":"Spanish"}
    ]
    return jsonify(languages)



@app.route("/postin", methods=['POST'])
def indexpost():
    data={"Name":"Kodjo","languages":"English"}
    return jsonify(data,{"message":"Data was received succesful."})

app.run(debug=True)





