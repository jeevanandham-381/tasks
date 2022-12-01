from flask import Flask,request, jsonify
import flk9_2

app = Flask(__name__)
@app.route('/')
def getdata():
    object=getdata.getData()
    aData=ObjectData.gatalldata()
    if len(aData):
        response=jsonify({
            "result":aData,
            "status":200
        })
    else:
        response=jsonify({
            "result":[],
            "status":400
        })

        return response
app.run("0.0.0.0",debug=True)
