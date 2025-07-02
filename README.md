🏨 Student Accommodation Management System

A user-friendly web application that streamlines the process of on-campus housing allocation in universities. Students can log in to search for available rooms, request accommodations, make reservations, and manage payments. Admins can monitor requests, assign rooms, and track transactions — all in one place.

This project ensures better data organization, security, and a more seamless experience for both students and administrators.

🧰 Tech Stack

Backend: Python (Flask)

Database: MongoDB (Atlas)

Frontend: HTML, CSS (Jinja2 templates)

Hosting: Render (Web Service)

🗄️ MongoDB Collections

The data is structured using separate MongoDB collections to simplify access and manipulation:


Admin	Stores admin login credentials and roles
Building	Contains details of each campus building
Rooms	Information about rooms in each building
Students	Student profiles and login data
Requests	Student room requests
Payment	Records of accommodation payments

📦 Features

🔐 Student login and dashboard

📝 Submit and track room requests

🧾 Admin panel to review and manage accommodations

🏢 Manage buildings and room inventories

💳 Simulated payment handling

📊 Modular backend for scalability


🛠 Local Setup (Improved)

1. Clone the Repository
git clone https://github.com/your-username/student-accommodation-system.git
cd student-accommodation-system

3. Create and Activate a Virtual Environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

4. Install Dependencies
pip install -r requirements.txt

5. Set Up Environment Variables
Create a .env file in the project root (do NOT commit this file):

MONGO_URI=your_mongodb_connection_string_here
Optionally, use the .env.example file as a template for environment variables (create this file if you want):

 .env.example
MONGO_URI=your_mongodb_connection_string_here
If your app uses python-dotenv (recommended), it will automatically load variables from .env.

5. Run the Application
Make sure your app.py runs the Flask app like this:

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    
Then start it:
python app.py

Open your browser at:
http://localhost:5000


⚠️ Common Issues

MongoDB Connection Errors:
Check if your MONGO_URI is correct, and whitelist your IP in MongoDB Atlas.

Port Already in Use:
Change the port in app.run() if 5000 is busy.

Environment Variables Not Loaded:
Ensure .env file exists and, if needed, you installed python-dotenv and imported it in your app.py like:

from dotenv import load_dotenv
load_dotenv()
