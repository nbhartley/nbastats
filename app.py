from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from models import db


@app.route('/')
def all_players():
     drinkers = db.session.query(models.Players).all()
     return render_template('first.html', players=players)
