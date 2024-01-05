import pytest
from application import app
from application.authors import controller

from application.authors.model import Author, Book

@pytest.fixture()
def create_author():
    author = Author('Britney', 20, 'fantasy')
    return author

@pytest.fixture()
def create_book():
    book = Book('Harry Potter', 'fantasy', 1)
    return book


@pytest.fixture
def api(monkeypatch):
    test_authors = [{'age': 20, 'genres': 'fantasy', 'id': 1, 'name': 'Britney', }, {'age': 23, 'genres': 'drama', 'id': 2, 'name': 'John'}]
    monkeypatch.setattr(controller, "authors", test_authors)
    api = app.test_client()
    return api
