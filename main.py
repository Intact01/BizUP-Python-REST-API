from flask import Flask
from flask_restful import Api, Resource, reqparse
from image_operations import *

app = Flask(__name__)
api = Api(app)

# to parse src
get_args = reqparse.RequestParser()
get_args.add_argument("src", help="Url of the image is required", required=True)


class ColorExtraction(Resource):
    def get(self):
        args = get_args.parse_args()    # get url from args
        src = args["src"]

        image = img_from_url(src)       # read image
        border, primary = get_colors(image)     # get border and primary colors
        return {"logo_border": border,
                "dominant_color": primary}


api.add_resource(ColorExtraction, "/")

# run the app
if __name__ == "__main__":
    app.run(debug=True)
