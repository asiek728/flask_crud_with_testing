def test_create_author(create_author):
    author = create_author

    assert author.name == 'Britney'
    assert author.age == 20
    assert author.genres == 'fantasy'

    assert author.__repr__() == f"Author(id: {author.id}, name: {author.name}, age: {author.age}, genres: {author.genres})"
    
    assert author.json == {
        "id": author.id,
        "name": author.name,
        "age": author.age,
        "genres": author.genres,
    }


def test_create_book(create_book):
    book = create_book

    assert book.name == 'Harry Potter'
    assert book.genre == 'fantasy'
    assert book.author_id == 1

    assert book.__repr__() == f"Book(id: {book.id}, name: {book.name}, genre: {book.genre})"
    
    assert book.json == {
        "id": book.id,
        "name": book.name,
        "genre": book.genre,
        "author_id": book.author_id
    }
