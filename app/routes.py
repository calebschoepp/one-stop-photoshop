from flask import render_template, url_for, flash, redirect
from app import app, db
from app.models import Post

@app.route('/')
@app.route('/index')
def index():
    posts = Post.query.all() # Builds a list
    return render_template('index.html', posts=posts, title='One Stop Photoshop')



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

@app.route('/post/<folder>')
def post(folder):
    post = Post.query.filter_by(folder=folder).first()
    return render_template('post.html', post=post, title='One Stop Photoshop')