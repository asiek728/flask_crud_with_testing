from application import db
from application.authors.model import Author

db.drop_all()
print("Dropping Database")

db.create_all()
print("Creating Database")

print("Seeding Database")
entry1 = Author(name="George R. R. Martin", age=75, genres="Fantasy, horror, science fiction")

entry2 = Author(name="J.K. Rowling", age=58, genres="Fantasy, drama, young adult fiction, crime fiction")

entry3 = Author(name="J. R. R. Tolkien", age=81, genres="Fantasy, high fantasy, mythopoeia, translation, literary criticism")

db.session.add_all([entry1, entry2, entry3])

db.session.commit()

print("Database creation successful")

