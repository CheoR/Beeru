from werkzeug.exceptions import abort

from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from src.auth import login_required
from src.db import get_db

bp = Blueprint('beer', __name__, url_prefix="/beer")

@bp.route('/<int:id>', methods=('GET',))
def index(id):
    db = get_db()

    reviews = db.execute("""
        SELECT r.*, u.username, b.abv, b.style, b.name, b.description, (
            SELECT SUM(r.rating)
            FROM review r
            JOIN beer b
                ON r.beer_id = b.id
                WHERE b.id = ?
        ) total_rating,
        (
            SELECT COUNT(r.rating)
            FROM review r
            JOIN beer b
                ON r.beer_id = b.id
                WHERE b.id = ?
        ) total_reviews,
        (
            SELECT ROUND(AVG(rating), 1)
            FROM review r
            JOIN beer b
                ON r.beer_id = b.id
                WHERE b.id = ?
        ) average_rating
        FROM BEER b
        JOIN review r
            ON b.id = r.beer_id
        JOIN user u
            ON r.author_id = u.id
        WHERE b.id = ?
        ORDER BY r.created DESC;
    """,
        (id, id, id, id)
    ).fetchall()
    return render_template('beer/detail.html', featured=reviews[0], reviews=reviews)
