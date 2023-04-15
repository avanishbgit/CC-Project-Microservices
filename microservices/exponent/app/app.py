from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
app.secret_key = '080_087_092_111'

class Exponent(Resource):
    def __init__(self):
        pass
    
    def get(self, n1, n2):
        try:
            return n1 ** n2
        except Exception as e:
            return str(e)

api.add_resource(Exponent, "/exp/<float(signed=True):n1>/<float(signed=True):n2>")

if __name__ == "__main__":
    app.run(
        debug = True,
        port = 5058,
        host = "0.0.0.0"
    )
