from flask import render_template, url_for, flash, redirect
from app import app, db
from app.models import Post
from random import randrange as rr

@app.route('/')
@app.route('/index')
def index():
    posts = Post.query.order_by(Post.folder).all() # Builds a list
    return render_template('index.html', posts=posts, title='One Stop Photoshop')



################### FIX
# @app.route('/next')
# def next():
#     return render_template('post.html', title='One Stop Photoshop')

# @app.route('/prev')
# def prev():
#     return render_template('post.html', title='One Stop Photoshop')

@app.route('/random')
def random():
    rand = rr(0, Post.query.count())
    post = Post.query.all()[rand]
    return redirect('post/{}'.format(post.folder))

@app.route('/post/<folder>')
def post(folder):
    post = Post.query.filter_by(folder=folder).first()
    return render_template('post.html', post=post, title='One Stop Photoshop')
