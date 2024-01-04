from application import db, app

app.app_context().push()

class Author(db.Model):
    __tablename__ = "authors"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    genres = db.Column(db.String(100), nullable=False)

    def __init__(self, name, age, genres):
        self.name = name
        self.age = age
        self.genres = genres

    def __repr__(self):
        return f"Author(id: {self.id}, name: {self.name}, age: {self.age}, genres: {self.genres})"
    
    @property
    def json(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "genres": self.genres
        }
