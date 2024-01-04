from application import db, app
from application.books.model import Book

app.app_context().push()

class Author(db.Model):
    #__tablename__ = "authors"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    genres = db.Column(db.String(100), nullable=False)
    books = db.relationship('Book', backref='author', lazy=True) #read data later

    def __init__(self, name, age, genres):
        self.name = name
        self.age = age
        self.genres = genres

    def __repr__(self):
        return f"Author(id: {self.id}, name: {self.name}, age: {self.age}, genres: {self.genres})"
    
    @property
    def json(self):
        books = []
        for book in self.books:
            books.append({"book ID": book.id, "name": book.name, "genre": book.genre})

        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "genres": self.genres,
            "books": books or "no books added yet"
        }


#
# class Book(db.Model):
#     #__tablename__ = "books"

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     genre = db.Column(db.String(35), nullable=False)
#     author_id = db.Column(db.Integer, db.ForeignKey('author.id'))

#     def __init__(self, name, genre, author_id):
#         self.name = name
#         self.genre = genre
#         self.author_id = author_id

#     def __repr__(self):
#         return f"Book(id: {self.id}, name: {self.name}, genre: {self.genre})"
    
#     @property
#     def json(self):
#         return {
#             "id": self.id,
#             "name": self.name,
#             "genre": self.genre,
#             "author_id": self.author_id
#         }
