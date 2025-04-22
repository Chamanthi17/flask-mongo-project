from flask import Flask, render_template
import os
from mongoengine import connect
from dotenv import load_dotenv
from Collections.Student import student_endpoints



app = Flask(__name__)
app.register_blueprint(student_endpoints)


@app.route('/')
def hello_world():
    return render_template("student_login.html")


@app.after_request
def add_header(response):
    response.cache_control.no_store = True
    return response



if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
