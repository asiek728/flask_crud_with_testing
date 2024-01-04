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
