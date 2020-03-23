from sqlalchemy import sql, orm
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy(app, session_options={'autocommit': False})

class Player(db.Model):
    __tablename__ = 'player'
    name = db.Column('name', db.String(20), primary_key=True)
