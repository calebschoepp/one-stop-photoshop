from flask import render_template, url_for, flash, redirect
from app import app, db
# from app.forms import AddGameForm
# from app.models import Game, Play

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')