from flask import request, Blueprint
from mongoengine import *

# Blueprint for payment endpoints
payment_endpoints = Blueprint('payment_endpoints', __name__,
                              template_folder='templates')

# Connect to MongoDB Atlas (replace <your-username> and <your-password>)
connect(host="mongodb+srv://user:user@cluster0.mwim6z3.mongodb.net/student-dorm?retryWrites=true&w=majority")

# MongoEngine Document for Payment
class Payment(Document):
    student_id = StringField()
    request_id = StringField()
    payment_type = StringField()
    amount = FloatField()
    payment_date = DateField()

# Route to add a new payment
@payment_endpoints.route("/payment/add", methods=['POST'])
def add_payment():
    if request.method == 'POST':
        # Get form data and create a new Payment object
        payment = Payment(request_id=request.form.get('request_id'),
                          student_id=request.form.get('student_id'),
                          payment_type=request.form.get('payment_type'),
                          amount=request.form.get('amount'),
                          payment_date=request.form.get('payment_date'))
        
        # Save the Payment object to the database
        payment.save()
        
        # Return the Payment ID
        return str(payment.id)
    else:
        print('Invalid request method')
