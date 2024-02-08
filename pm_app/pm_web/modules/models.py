from .. import db, login_manager
from datetime import datetime
from flask_login import UserMixin
from itsdangerous import URLSafeTimedSerializer as Serializer


@login_manager.user_loader
def load_user(user_id):
    return user.objects(id=user_id).first()

class user(db.Document, UserMixin):
    name =  db.StringField(required=True, unique=True, min_length=0, max_length=30)
    email = db.EmailField(unique=True, required=True, max_length=100)
    image_file =  db.StringField(required=True, max_length=120, default='default.jpg')
    password = db.StringField(max_length=20, required=True)
    partners = db.ListField(db.EmailField())

    def __repr__():
        return f"User(name={self.name}, email={self.email}, password={self.password}, image_file={self.image_file})"


class project(db.Document, UserMixin):
    project_name = db.StringField(required=True, unique=True, max_length=15)
    date = db.StringField(max_length=30, required=True, default=datetime.utcnow)
    description = db.StringField(max_length=200, required=True)
    cover_image = db.StringField(required=True, max_length=120, default='cover_default.jpg')

    def __repr__(self):
        return f"User(project_name={self.project_name}, date={self.date}, description={self.description}, cover_image={self.cover_image})"

