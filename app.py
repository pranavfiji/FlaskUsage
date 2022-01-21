from crypt import methods
from dataclasses import dataclass
from flask import Flask, jsonify, request
app = Flask(__name__)

data=[{
    
    "Landline" :"12345",
    "Name":"Pranav",
    "done":False,
    "id":1,



} ,
{
    "Landline" :"12345",
    "Name":"Johny",
    "done":False,
    "id":2,
}
]
@app.route("/add-data", methods = ["POST"])

def addData():
    if not request.json:
        return jsonify({
            "status" : "error",
            "message" : "please input more data"

        },400)

    datas={
        "id" : task[-1]["id"]+1,
        "title":request.json["title"],
        "done":False

    }

    data.append(datas)

def getTask():
    return jsonify({
        "data" :data
    })

if(__name__ == "__main__"):
    app.run(debug=True)