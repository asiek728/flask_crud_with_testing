from application import db
from application.authors.model import Author   
from application.books.model import Book

db.drop_all()
print("Dropping Database")

db.create_all()
print("Creating Database")

print("Seeding Database")
entry1 = Author(name="George R. R. Martin", age=75, genres="Fantasy, horror, science fiction")

entry2 = Author(name="J.K. Rowling", age=58, genres="Fantasy, drama, young adult fiction, crime fiction")

entry3 = Author(name="J. R. R. Tolkien", age=81, genres="Fantasy, high fantasy, mythopoeia, translation, literary criticism")

db.session.add_all([entry1, entry2, entry3])

book1 = Book(name="Game of Thrones", genre="Fantasy", author_id=1)

book2 = Book(name="The Winds of Winter", genre="Fantasy", author_id=1)

book3 = Book(name="Hobbit", genre="Fantasy", author_id=3)

db.session.add_all([book1, book2, book3])

db.session.commit()

print("Database creation successful")

