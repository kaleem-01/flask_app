from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_track_usage import TrackUsage
from flask_track_usage.storage.sql import SQLStorage


app = Flask(__name__)

#
# Setup SQLite database
#
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)



# def db_drop_and_create_all(app):
#     with app.app_context():
#         db.drop_all()
#         db.create_all()
#
# db_drop_and_create_all(app)

# TrackUsage Setup
#
app.config["TRACK_USAGE_USE_FREEGEOIP"] = True
app.config['TRACK_USAGE_INCLUDE_OR_EXCLUDE_VIEWS'] = 'include'
with app.app_context():
    pstore = SQLStorage(db=db)
t = TrackUsage(app, [pstore])

from routes import *


# class Data(db.Model):
#     id = db.Column(db.Integer, primary_key= True)
#     first_name = db.Column(db.String(200), nullable = False)
#     last_name = db.Column(db.String(200), nullable = False)
#     date_created = db.Column(db.DateTime, default = datetime.utcnow)
#
#     def __repr__(self):
#         pass



if __name__ == '__main__':
    app.run(port=4000, debug = True)
