from app import app
from db import db

db.init_app(app)

# important to import what you want to be in the database such as Item and Store models if you want them as tables in the database
# SQLAlchemy creates the data.db for us but it doesn't put any tables in it, sp were going to tell to do so
@app.before_first_request # before the first request runs it will do the code below
def create_tables():
    db.create_all()
