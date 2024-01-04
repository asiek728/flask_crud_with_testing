from flask import jsonify, request
from werkzeug import exceptions
from .model import Author
from .. import db


def index():
    authors = Author.query.all()
    try:
        return jsonify({ "data": [c.json for c in authors] }), 200
    except:
        raise exceptions.InternalServerError(f"Something went wrong")


def create():
    try:
        name, age, genres = request.json.values()

        new_author = Author(name, age, genres)

        db.session.add(new_author)
        db.session.commit()

        return jsonify({ "data": new_author.json }), 201
    except:
        raise exceptions.BadRequest(f"We couldn't add this author")
