from application import app
from flask import jsonify

@app.route('/')
def hello():
    return jsonify({
        "message": "Welcome",
        "description": "Books API",
        "endpoints": [
            "GET /",
            "GET /authors",
            "GET /authors/<int:id>",
            "POST /authors",
            "PATCH /authors/<int:id>",
            "DELETE /authors/<int:id>"
        ]
    }), 200
