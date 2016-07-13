from flask import Flask, render_template, request, redirect
from db import db_all, db_delete, db_new, db_post, db_update

app = Flask(__name__)


@app.route('/')
def index():
    list_posts = list(reversed(db_all()))
    return render_template('index.html', posts=list_posts)


@app.route('/new_post')
def create():
    return render_template('create-post.html')


@app.route('/add_post', methods=['POST'])
def add_post():
    title = request.form['title']
    body = request.form['body']
    if title != "" and body != "":
        db_new(title=title, body=body)
    return redirect('/')


@app.route('/post<id>', methods=['GET'])
def get_post(id):
    post = db_post(id)
    return render_template('post.html', post=post)


@app.route('/update<id>', methods=['GET', 'POST'])
def update(id):
    if request.method == 'GET':
        post = db_post(id)
        return render_template('update.html', post=post)
    elif request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        updated_post = db_update(id, title, body)
        return render_template('post.html', post=updated_post)

if __name__ == '__main__':
    app.run()
