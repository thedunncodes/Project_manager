# The Database model for the project manangement web app

from tkinter import CASCADE
from .. import db, login_manager
from datetime import datetime
from flask_login import UserMixin
from itsdangerous import URLSafeTimedSerializer as Serializer


@login_manager.user_loader
def load_user(user_id):
    return user.objects(id=user_id).first()

class user(db.Document, UserMixin):
    ''' This is a database model that is used to store a user's data with the 
        the help of Flask_login UserMixin
    '''
    name =  db.StringField(required=True, unique=True, min_length=0, max_length=30)
    email = db.EmailField(unique=True, required=True, max_length=100)
    image_file =  db.StringField(required=True, max_length=120, default='default.jpg')
    password = db.StringField(max_length=20, required=True)
    partners = db.ListField(db.EmailField())
    project_id = db.ListField(db.ReferenceField('project', register_delete_rule=0), default=[])

    def __repr__(self):
        return f"User(name={self.name}, email={self.email}, password={self.password}, image_file={self.image_file}, project_id={self.project_id})"


class project(db.Document, UserMixin):
    ''' This is a database model that is used to store user projects with the 
        the help of Flask_login UserMixin
    '''
    project_name = db.StringField(required=True, unique=True, max_length=15)
    date = db.DateTimeField(required=True, default=datetime.utcnow())
    description = db.StringField(required=True, unique=True, max_lenght=50)
    cover_image = db.StringField(required=True, max_length=120, default='cover_default.jpg')
    color = db.StringField(required=True, unique=True)
    task_id = db.ListField(db.ReferenceField('task', register_delete_rule=0), default=[])


    def __repr__(self):
        return f"User_project(project_name={self.project_name}, date={self.date}, description={self.description}, color={self.color} cover_image={self.cover_image}, task_id={self.task_id})"

class task(db.Document, UserMixin):
    ''' This is a database model that is used to store tasks under a project with the 
        the help of Flask_login UserMixin
    '''
    task = db.StringField(required=True, unique=True)
    priority = db.StringField(required=True)
    status = db.StringField(required=True, default="Ongoing")

    def __repr__(self):
        return f"Tasks(task_name={self.task}, priority={self.priority}, status={self.status})"