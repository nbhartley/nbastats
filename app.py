from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 's3cr3t'
app.config.from_object('config')
db = SQLAlchemy(app, session_options={'autocommit': False})

import models

@app.route('/')
def all_players():
     players = db.session.query(models.Player).all()
     return render_template('first.html', players=players)

@app.route('/<some_player>')
def some_player_page(some_player):

	return render_template('player.html, player=')