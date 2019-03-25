from flask_restful import Resource
from flask import jsonify, request
from mongoengine.errors import NotUniqueError, ValidationError
from apps.messages import MSG_RESOURCE_CREATED
from .models import Post
from .schemas import PostSchema

from apps.responses import (
    resp_already_exists,
    resp_exception,
    resp_data_invalid,
    resp_ok,
    resp_does_not_exist
)

class Route(Resource):
    def post(self):
        body = request.get_json()

        if body is None:
            return resp_data_invalid('Posts', [])

        schema = PostSchema()
        data, errors = schema.load(body)

        if errors:
            return resp_data_invalid('Posts', errors)

        try:                
            model = Post(**data)
            model.save()

        except NotUniqueError:
            return resp_already_exists('Posts', '')

        except ValidationError as e:
            return resp_exception('Posts', str(e))

        except Exception as e:
            return resp_exception('Posts', str(e))

        result = schema.dump(model)

        return resp_ok(
            'Posts', MSG_RESOURCE_CREATED.format('Post'),  data = result.data,
        )

    def get(self):
        return resp_ok(
            'Posts', '',  data = Post.objects.all()
        )

class Route_with_id(Resource):
    def get(self, id):
        try:
            post = Post.objects.get(id=id)
        
        except ValidationError as e:
            return resp_exception('Posts', str(e))

        except Post.DoesNotExist as e:
            return resp_does_not_exist('Posts', str(e))

        except Exception as e:
            return resp_exception('Posts', str(e))
            
        return resp_ok(
            'Posts', '',  data = post
        )

    def delete(self, id):
        try:
            post = Post.objects.get(id=id)
            if post:
                delete = post.delete()
                
                return resp_ok(
                    'Posts', '',  data = delete
                )
        
        except ValidationError as e:
            return resp_exception('Posts', str(e))

        except Post.DoesNotExist as e:
            return resp_does_not_exist('Posts', str(e))

        except Exception as e:
            return resp_exception('Posts', str(e))

    def put(self, id):
        try:
            body = request.get_json()

            if body is None:
                return resp_data_invalid('Posts', [])

            post = Post.objects.get(id=id)

            if post:
                update = post.update(**body)

                return resp_ok(
                    'Posts', '',  data = update
                )
        
        except ValidationError as e:
            return resp_exception('Posts', str(e))

        except Post.DoesNotExist as e:
            return resp_does_not_exist('Posts', str(e))

        except Exception as e:
            return resp_exception('Posts', str(e))