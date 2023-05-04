from flask import Flask, render_template, request, url_for
from markupsafe import escape

app = Flask(__name__)
app.jinja_env.auto_reload = True
app.config["TEMPLATES_AUTO_RELOAD"] = True

DATA = [
    {"name": "Beer1", "flavor": "bold"},
    {"name": "Beer2", "flavor": "flat"},
    {"name": "Beer3", "flavor": "nutty"},
    {"name": "Beer4", "flavor": "hoppy"},
]

REVIEW = [
    { "user": "user1", "review": "Beer1 is ", "stars": 5},
    { "user": "user2", "review": "Beer2 was ", "stars": 1},
    { "user": "user3", "review": "Beer3 yup", "stars": 3},
    { "user": "user4", "review": "Beer4 i like ", "stars": 1},
]

@app.route('/')
def index():
    return render_template('index.html', route="home", data=DATA, review=REVIEW )

@app.route('/about')
def about():
    return render_template('about.html', route="about")

@app.route('/beers')
def beer():
    return render_template('beers.html', route="beers")

@app.errorhandler(404)
def page_not_found(err):
    return render_template('404.html'), 404

# @app.route('/pug')
# def pug():
#     return "<p>PUG</p>"

# @app.route('/user/<username>')
# def show_user_profile(username):
#     # show the user profile for that user
#     return f'User {escape(username)}'

# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     print(f"got {post_id}")
#     # show the post with the given id, the id is an integer
#     return f'Post {post_id}'

# @app.route('/path/<path:subpath>')
# def show_subpath(subpath):
#     # show the subpath after /path/
#     return f'Subpath {escape(subpath)}'

# with app.test_request_context():
#     print(url_for('pug', next='/'))
#     # /pug?next=%2F

# def do_the_login():
#     print('it was a POST request')
#     return 'it was a POST request'

# def show_the_login_form():
#     print('it was a GET request')
#     return 'it was a POST request'

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         return do_the_login()
#     else:
#         return show_the_login_form()

# @app.get('/another-login')
# def login_get():
#     return show_the_login_form()

# @app.post('/another-login')
# def login_post():
#     return do_the_login()

# @app.route('/hello/')
# @app.route('/hello/<name>')
# def hello(name=None):
#     return render_template('hello.html', name=name)