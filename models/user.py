from database import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    # id (int), username (text), password (text)
    id = db.Column(db.Integer, primary_key=True) 
    # map the ORM attribute `username` to the existing DB column named 'usarname'
    username = db.Column('usarname', db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)

