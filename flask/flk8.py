import json

from flask import Flask,jsonify,request

app = Flask(__name__)

@app.route('/returnjson', methods = ['GET'])
def ReturnJSON():
    if(request.method == 'GET'):
        data = {"name":"jeeva"}
        return jsonify(data)

if __name__=='__main__':
	app.run(debug=True)
        

#tom and jerry
