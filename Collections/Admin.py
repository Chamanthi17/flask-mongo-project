from flask import request, Blueprint
from mongoengine import *

# Set up Flask Blueprint
admin_endpoints = Blueprint('admin_endpoints', __name__,
                            template_folder='templates')

# MongoDB Atlas connection string (replace <username>, <password>, and <dbname>)
connect(host="mongodb+srv://user:user@cluster0.mwim6z3.mongodb.net/student-dorm?retryWrites=true&w=majority")

# MongoEngine Document (Admin model)
class Admin(Document):
    admin_id = StringField()
    name = StringField()
    email = StringField()
    password = StringField()

# Route to add a new admin
@admin_endpoints.route("/admin/add", methods=['POST'])
def add_user():
    if request.method == 'POST':
        # Get form data and create a new Admin object
        admin = Admin(admin_id=request.form.get('name'),
                      name=request.form.get('name'),
                      email=request.form.get('email'),
                      password=request.form.get('password'))
        
        # Save the Admin object to the database
        admin.save()
        
        # Return the Admin ID
        return str(admin.id)
    else:
        print('Invalid request method')
