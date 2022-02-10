from flask import Flask
from flask_migrate import Migrate

# primeira forma
# mg = Migrate()

# def init_app(app: Flask):
#     mg.init_app(app=app, db=app.db)

# segunda forma
def init_app(app: Flask):
    Migrate(app=app, db=app.db, compare_type=True)