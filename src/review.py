from werkzeug.exceptions import abort

from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from src.auth import login_required
from src.db import get_db

bp = Blueprint('review', __name__, url_prefix="/review")

def get_review(id, check_author=True):
    review = get_db().execute("""
            SELECT r.id, r.title, r.comment, r.created, r.rating, r.author_id, u.username
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

@bp.route('/', methods=('GET', 'POST'))
@login_required
def index():
    db = get_db()

    if request.method == 'POST':
        beer_id = int(request.form['selection'])
        title = request.form['title']
        comment = request.form['comment']
        rating = request.form['rating']
        error = None

        if not title:
            error = 'Title required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO review (title, comment, beer_id, author_id, rating)'
                ' VALUES (?, ?, ?, ?, ?)',
                (title, comment, beer_id, g.user['id'], rating)
            )
            db.commit()
            return redirect(url_for('review.index'))

    reviews = db.execute("""
        SELECT r.id, r.title, r.comment, r.created, r.rating, u.username, r.author_id
        FROM review r
        JOIN user u
            ON r.author_id = u.id
		WHERE u.id = ?
        ORDER BY r.created DESC;
    """,
    (g.user['id'],)
    ).fetchall()

    beers = db.execute("""
    SELECT b.id, b.name, b.description, b.number_of_review, b.total_rating, u.username, r.title, r.comment, r.rating, r.created
    FROM review as r
    INNER JOIN user as u
        ON u.id == r.author_id
    INNER JOIN beer as b
        ON r.beer_id == b.id
    GROUP BY b.id;
    """).fetchall()

    return render_template('review/index.html', route="review", beers=beers, reviews=reviews)

@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    review = get_review(id)

    if request.method == 'POST':
        title = request.form['title']
        comment = request.form['comment']
        rating = request.form['rating']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute("""
                    UPDATE review
                    SET title = ?, comment = ?, rating = ?
                    WHERE id = ?
                """,
                (title, comment, rating, id)
            )
            db.commit()
            return redirect(url_for('review.index'))

    return render_template('review/update.html', review=review)
