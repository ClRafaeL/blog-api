from datetime import datetime
from apps.db import db
from mongoengine import (
    DateTimeField,
    StringField
)

class PostMixin(db.Document):
    meta = {
        'abstract': True,
        'ordering': ['created']
    }

    author = StringField(required=True)
    category = StringField(required=True)
    title = StringField(required=True)
    text = StringField()
    created = DateTimeField(default=datetime.now)

class Post(PostMixin):
    meta = {'collection': 'posts'}

    