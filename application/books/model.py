from application import db, app
#from application.authors.model import Author
app.app_context().push()

class Book(db.Model):
    #__tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(35), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)

    def __init__(self, name, genre, author_id):
        self.name = name
        self.genre = genre
        self.author_id = author_id

    def __repr__(self):
        return f"Book(id: {self.id}, name: {self.name}, genre: {self.genre})"
    
    @property
    def json(self):
        return {
            "id": self.id,
            "name": self.name,
            "genre": self.genre,
            "author_id": self.author_id
        }
