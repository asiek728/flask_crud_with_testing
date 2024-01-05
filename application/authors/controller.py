from flask import jsonify, request
from werkzeug import exceptions
from .model import Author
from .. import db

authors = []
def index():
    authors = Author.query.all()
    try:
        return jsonify({ "data": [c.json for c in authors] }), 200
    except:
        raise exceptions.InternalServerError(f"Something went wrong")
    
def show(id):
    authors = Author.query.filter_by(id=id).first()
    try:
        return jsonify({ "data": authors.json }), 200
    except:
        raise exceptions.NotFound(f"Author not found")

def create():
    try:
        name, age, genres = request.json.values()

        new_author = Author(name, age, genres)

        db.session.add(new_author)
        db.session.commit()

        return jsonify({ "data": new_author.json }), 201
    except:
        raise exceptions.BadRequest(f"We couldn't add this author")

def update(id):
    data = request.json
    author = Author.query.filter_by(id=id).first()

    for (attribute, value) in data.items():
        if hasattr(author, attribute):
            setattr(author, attribute, value)

    db.session.commit()
    return jsonify({ "data": author.json })

def destroy(id):
    author = Author.query.filter_by(id=id).first()
    db.session.delete(author)
    db.session.commit()
    return "Author has been deleted", 204
