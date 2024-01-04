import pytest
from application.authors.model import Author, Book

@pytest.fixture(scope='module')
def create_author():
    author = Author('Britney', 20, 'fantasy')
    return author

@pytest.fixture(scope='module')
def create_book():
    book = Book('Harry Potter', 'fantasy', 1)
    return book
