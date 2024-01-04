from flask import jsonify, request
from werkzeug import exceptions
from .model import Book
from .. import db


def index():
    books = Book.query.all()
    try:
        return jsonify({ "data": [c.json for c in books] }), 200
    except:
        raise exceptions.InternalServerError(f"Something went wrong")
    
def show(id):
    books = Book.query.filter_by(id=id).first()
    try:
        return jsonify({ "data": books.json }), 200
    except:
        raise exceptions.NotFound(f"Book not found")

def create():
    try:
        name, genre, author_id = request.json.values()

        new_book = Book(name, genre, author_id)

        db.session.add(new_book)
        db.session.commit()

        return jsonify({ "data": new_book.json }), 201
    except:
        raise exceptions.BadRequest(f"We couldn't add this book")

def update(id):
    data = request.json
    book = Book.query.filter_by(id=id).first()

    for (attribute, value) in data.items():
        if hasattr(book, attribute):
            setattr(book, attribute, value)

    db.session.commit()
    return jsonify({ "data": book.json })

def destroy(id):
    book = Book.query.filter_by(id=id).first()
    db.session.delete(book)
    db.session.commit()
    return "Book has been deleted", 204
