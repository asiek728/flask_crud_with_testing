def test_create_author(create_author):
    author = create_author

    assert author.name == 'Britney'
    assert author.age == 20
    assert author.genres == 'fantasy'

def test_repr_author(create_author):
    author = create_author

    assert author.__repr__() == f"Author(id: {author.id}, name: {author.name}, age: {author.age}, genres: {author.genres})"
    

def test_json_author(create_author):
    author = create_author
    books = []

    assert author.json == {
        "id": author.id,
        "name": author.name,
        "age": author.age,
        "genres": author.genres,
        "books": books or "no books added yet"
    }
