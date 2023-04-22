from flask import Flask, render_template, request, url_for
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return "<p>I'm a little piggy</p>"

@app.route('/pug')
def pug():
    return "<p>PUG</p>"


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    print(f"got {post_id}")
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'

with app.test_request_context():
    print(url_for('pug', next='/'))
    # /pug?next=%2F

def do_the_login():
    print('it was a POST request')
    return 'it was a POST request'

def show_the_login_form():
    print('it was a GET request')
    return 'it was a POST request'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()

@app.get('/another-login')
def login_get():
    return show_the_login_form()

@app.post('/another-login')
def login_post():
    return do_the_login()

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)