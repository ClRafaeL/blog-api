from flask_restful import Api
from .posts.resources import Route_with_id, Route

api = Api()

def configure_api(app):
    api.add_resource(Route, '/posts/')
    api.add_resource(Route_with_id, '/posts/<id>')
    api.init_app(app)