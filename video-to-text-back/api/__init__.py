from flask_restx import Api

from .get_video import api as ns1

api = Api(
    title='Video to text API',
    version='1.0',
    description='команда "Крафтовый код"',
)

api.add_namespace(ns1)
