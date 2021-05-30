from flask import Flask, request
from flask_restful import Api, Resource, reqparse
from image_operations import *

app = Flask(__name__)
api = Api(app)

get_args = reqparse.RequestParser()
get_args.add_argument("src", help="Url of the image is required", required=True)


class ColorExtraction(Resource):
    def get(self):
        args = get_args.parse_args()
        src = args["src"]
        image = img_from_url(src)
        border, primary = get_colors(image)
        return {"border": border,
                "primary": primary}


api.add_resource(ColorExtraction, "/")

if __name__ == "__main__":
    app.run(debug=True)
