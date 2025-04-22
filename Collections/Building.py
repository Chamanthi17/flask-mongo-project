from flask import Blueprint
from mongoengine import *

# Blueprint for building endpoints
building_endpoints = Blueprint('building_endpoints', __name__,
                               template_folder='templates')

# Connect to MongoDB Atlas using your connection string
connect(host="mongodb+srv://<user>:<user>@cluster0.mwim6z3.mongodb.net/?retryWrites=true&w=majority")

# MongoEngine Document for Building
class Building(Document):
    building_number = StringField()
    gender = StringField()
    rooms_available = ListField()
