from flask import Flask,jsonify,redirect,url_for,render_template
import requests

app=Flask(__name__)

@app.route("/")
def home():
    return "API CREATE TEST"

@app.route('/index', methods=['POST','GET'])
def indexpost():
    return render_template('http://127.0.0.1:5000/index')

@app.route('/index1',)
def user(usr):
    return "POST"



if __name__ == "__main__":
    app.run(debug=True)


 




