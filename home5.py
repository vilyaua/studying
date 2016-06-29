"""
Daniel Omelchenko, [21.06.16 11:15]
посмотри Flask

Daniel Omelchenko, [21.06.16 11:16]
сделай маленький веб сервер , который будет отдавать по HTTP://127.0.0.1:5000/

Daniel Omelchenko, [21.06.16 11:16]
hello world
"""

from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def hello():
    return "Booo"

@app.route("/add", methods = ["POST"])
def adding():
    return str(request.get_json()["a"] + request.get_json()["b"])

@app.route("/div", methods = ["POST"])
def dividing():
    if request.get_json()["b"] == 0: 
        return("Divizion by ZERO")
    return str(request.get_json()["a"] / request.get_json()["b"])

if __name__ == "__main__":
    app.run()
