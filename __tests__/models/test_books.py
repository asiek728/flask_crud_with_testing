def test_create_book(create_book):
    book = create_book

    assert book.name == 'Harry Potter'
    assert book.genre == 'fantasy'
    assert book.author_id == 1


def test_repr_book(create_book):
    book = create_book

    assert book.__repr__() == f"Book(id: {book.id}, name: {book.name}, genre: {book.genre})"
    

def test_json_book(create_book):
    book = create_book
    
    assert book.json == {
        "id": book.id,
        "name": book.name,
        "genre": book.genre,
        "author_id": book.author_id
    }
