from flask import Flask, render_template, redirect, url_for
//from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
//app.secret_key = '123'
//app.config.from_object('config')
//db = SQLAlchemy(app, session_options={'autocommit': False})

@app.route('/')
def all_players():
    return render_template('first.html')