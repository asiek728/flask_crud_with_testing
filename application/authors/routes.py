from flask import request
from werkzeug import exceptions
from application import app # app from __init__.
from .controller import index, create#, show, update, destroy

@app.route('/authors', methods=["GET", "POST"])
def handle_authors():
    if request.method == "POST": return create()
    if request.method == "GET": return index()
