from distutils.log import debug
from flask import Flask
from flask_restful import Resources, Api

App = Flask(__name__)

api.add_resource(helloworld,'/helloworld')

if __name__ == "__main__":
    app.run(debug=True)
