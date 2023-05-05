from werkzeug.exceptions import abort

from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from src.auth import login_required
from src.db import get_db

bp = Blueprint('review', __name__, url_prefix="/reviews")

def get_review(id, check_author=True):
    review = get_db().execute("""
            SELECT r.id, r.title, r.comment, r.created, r.rating, author_id, username
            FROM review r
            JOIN user u
            ON r.author_id = u.id
            WHERE u.id = ?;
        """,
        (id,)
    ).fetchone()

    if review is None:
        abort(404, f"Review id {id} doesn't exist.")

    # check_author used to get a review without checking the author.
    # useful if you wrote a view to show an individual review on a page,
    # where the user doesn’t matter because they’re not modifying the
    # review.
    if check_author and review['author_id'] != g.user['id']:
        abort(403)

    return review

@bp.route('/')
@login_required
def index():
    db = get_db()
    reviews = db.execute("""
        SELECT r.id, r.title, r.comment, r.created, r.rating, author_id, username
        FROM review r
        JOIN user u
        ON r.author_id = u.id
        ORDER BY created DESC;
    """
    ).fetchall()
    return render_template('review/index.html', route="reviews", reviews=reviews)
