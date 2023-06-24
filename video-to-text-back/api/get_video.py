import json
import sys

from flask_restx import Namespace, Resource, abort

sys.path.append("..")

from main_compiler import main

api = Namespace('get video', description='Get data from video')

parser = api.parser()
parser.add_argument('link', type=str, required=True)
parser.add_argument('model', type=str, required=False, default='base')


@api.route('/')
@api.expect(parser)
class BigData(Resource):
    @api.response(404, 'Not a valid link...')
    @api.response(200, 'Success')
    def post(self):
        args = parser.parse_args()

        link = args["link"]
        model = args["model"]

        if link is not None:
            result = main(link, model)
            if result is not None:
                filename = f"download_video/{result['metadata']['title']}.json"
                print(filename)
                with open(filename, "w") as write_file:
                    json.dump(result, write_file)
                return result, 200
            else:
                return f"{link} is not a valid link.", 404
