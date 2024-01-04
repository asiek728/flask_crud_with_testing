# from flask import Flask, jsonify
# from flask_sqlalchemy import SQLAlchemy
# from flask_testing import TestCase
# from application import app, db, create_app

# def create_test_app():
#     app = Flask(__name__)
#     app.config['TESTING'] = True
#     app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://gskxgcwq:QwiVyTkjieyQ0l0X19Uv--oQnLF58Tjb@tyke.db.elephantsql.com/gskxgcwq"
#     # Dynamically bind SQLAlchemy to application
#     db.init_app(app)
#     app.app_context().push() # this does the binding
#     return app


# class MyTest(TestCase):

#     # I removed some config passing here
#     def create_app(self):
#         return create_test_app()

#     def setUp(self):
#         db.create_all()

#     def tearDown(self):

#         db.session.remove()
#         db.drop_all()


# @app.route("/")
# def some_json():
#     return jsonify(success=True)

# class TestViews(TestCase):
#     def test_some_json(self):
#         response = self.client.get("/")
#         self.assertEquals(response.json, dict(success=True))
