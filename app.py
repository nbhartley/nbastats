from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import models

app = Flask(__name__)
app.secret_key = 's3cr3t'
app.config.from_object('config')
db = SQLAlchemy(app, session_options={'autocommit': False})

@app.route('/')
def all_players():
     drinkers = db.session.query(models.Players).all()
    return render_template('first.html', players=players)
