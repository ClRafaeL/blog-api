from marshmallow import Schema
from marshmallow.fields import Str
from apps.messages import MSG_FIELD_REQUIRED

class PostSchema(Schema):
    author = Str(required=True, error_messages={'required': MSG_FIELD_REQUIRED})
    title = Str(required=True, error_messages={'required': MSG_FIELD_REQUIRED})
    category = Str(required=True, error_messages={'required': MSG_FIELD_REQUIRED})
    text = Str(required=True, error_messages={'required': MSG_FIELD_REQUIRED})
