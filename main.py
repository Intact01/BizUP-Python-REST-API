from flask import Flask
from flask_restful import Api, Resource, abort

app = Flask(__name__)
api = Api(app)


class ColorExtraction(Resource):
    def get(self, src):
        return


api.add_resource(ColorExtraction, "/<str:src>")
