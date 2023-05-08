from werkzeug.exceptions import abort
from markupsafe import escape
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from src.db import get_db


bp = Blueprint('page', __name__)

@bp.route('/')
def index():
    db = get_db()
    reviews = db.execute("""
        SELECT r.id, b.name as beer, u.username, r.title, r.comment, r.rating, r.created, r.author_id
        FROM review as r
        INNER JOIN user as u
            ON u.id == r.author_id
        INNER JOIN beer as b
            ON r.beer_id == b.id
        ORDER BY r.created DESC
        LIMIT 12;
    """).fetchall()

    beers = db.execute("""
        SELECT b.*, SUM(r.rating) as total_rating, COUNT(rating) as total_reviews, ROUND(AVG(rating), 1) as average_rating
        FROM BEER b
        JOIN review r
            ON b.id = r.beer_id
        GROUP BY r.beer_id;
    """).fetchall()
    return render_template('page/index.html', route="home", beers=beers, reviews=reviews )

@bp.route('/about')
def about():
    return render_template('page/about.html', route="about")

@bp.route('/beers')
def beer():
    return render_template('page/beers.html', route="beers")

@bp.app_errorhandler(404)
def page_not_found(err):
    return render_template('404.html'), 404

# @bp.route('/pug')
# def pug():
#     return "<p>PUG</p>"

# @bp.route('/user/<username>')
# def show_user_profile(username):
#     # show the user profile for that user
#     return f'User {escape(username)}'

# @bp.route('/post/<int:post_id>')
# def show_post(post_id):
#     print(f"got {post_id}")
#     # show the post with the given id, the id is an integer
#     return f'Post {post_id}'

# @bp.route('/path/<path:subpath>')
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

# @bp.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         return do_the_login()
#     else:
#         return show_the_login_form()

# @bp.get('/another-login')
# def login_get():
#     return show_the_login_form()

# @bp.post('/another-login')
# def login_post():
#     return do_the_login()

# @bp.route('/hello/')
# @bp.route('/hello/<name>')
# def hello(name=None):
#     return render_template('hello.html', name=name)
