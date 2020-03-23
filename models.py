from sqlalchemy import sql, orm
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.secret_key = 's3cr3t'
app.config.from_object('config')
db = SQLAlchemy(app, session_options={'autocommit': False})

db = SQLAlchemy(app, session_options={'autocommit': False})

class Player(db.Model):
    __tablename__ = 'player'
    name = db.Column('name', db.String(20), primary_key=True)
