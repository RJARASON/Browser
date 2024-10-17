from flask import Flask,jsonify,request
import requests

app=Flask(__name__)

@app.route("/index1", methods=['POST'])
def indexpost():
    data={"Name":"Kodjo","languages":"English"}
    datarequest=requests.post("http://127.0.0.1:5000/index1",data=data)
    return jsonify(datarequest)

app.run(debug=True)