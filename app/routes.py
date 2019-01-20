from flask import render_template, url_for, flash, redirect
from app import app, db
# from app.forms import AddGameForm
# from app.models import Game, Play

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='One Stop Photoshop')



################### FIX
@app.route('/next')
def next():
    return render_template('post.html', title='One Stop Photoshop')

@app.route('/prev')
def prev():
    return render_template('post.html', title='One Stop Photoshop')

@app.route('/random')
def random():
    return render_template('post.html', title='One Stop Photoshop')

@app.route('/post')
def post():
    return render_template('post.html', title='One Stop Photoshop')