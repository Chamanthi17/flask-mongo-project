from flask import request
from mongoengine import *
from Collections.Building import *

# Blueprint for room endpoints
room_endpoints = Blueprint('room_endpoints', __name__,
                           template_folder='templates')

# Connect to MongoDB Atlas (replace <your-username> and <your-password>)
connect(host="mongodb+srv://user:user@cluster0.mwim6z3.mongodb.net/student-dorm?retryWrites=true&w=majority")

is_setup_done = False

# MongoEngine Document for Room
class Room(Document):
    room_number = IntField()
    room_type = StringField()
    price_per_semester = IntField()
    building_number = StringField()
    is_vacant = DictField()
    max_count = IntField()
    occupants = DictField()

# Route to add a new room
@room_endpoints.route("/room/add", methods=['POST'])
def add_payment():
    if request.method == 'POST':
        room = Room(room_number=request.form.get('room_number'),
                    room_type=request.form.get('room_type'),
                    price_per_semester=request.form.get('price_per_semester'),
                    building_number=request.form.get('building_number'),
                    is_vacant=dict(),
                    occupants=dict())
        room.save()
        return str(room.id)
    else:
        print('Invalid request method')

# Function to get all vacant rooms
def get_all_vacant_rooms():
    data = dict()
    data['2B'] = []
    data['3B'] = []
    for room in Room.objects():
        data[room.room_type] += [room]
    return data

# Function to get all rooms
def get_all_rooms():
    return Room.objects()

# Function to assign a room
def assign_room(student_id, room_number, semester):
    room = Room.objects(room_number__exact=room_number)[0]
    room.occupants[semester].append(student_id)
    if room.max_count == len(room.occupants[semester]):
        room.is_vacant[semester] = False
    room.save()
    return room.price_per_semester

# Setup data (rooms and buildings)
def setup_data():
    male_building = Building(building_number='M1', gender='Male',
                             rooms_available=[101, 102, 103, 104, 105, 106, 107, 108, 109, 110])
    male_building.save()
    female_building = Building(building_number='F1', gender='Female',
                               rooms_available=[201, 202, 203, 204, 205, 206, 207, 208, 209, 210])
    female_building.save()
    print('Setup rooms data')
    for building in Building.objects():
        start = 101 if building.building_number == 'M1' else 201
        for room_number in range(start, start + 10, 1):
            vacant_data = dict()
            occupants_data = dict()
            for semester in ('Fall 2023', 'Spring 2024', 'Fall 2024', 'Spring 2025', 'Fall 2025'):
                vacant_data[semester] = True
                occupants_data[semester] = []

            room = Room(room_number=room_number,
                        room_type='2B' if room_number % 2 == 0 else '3B',
                        price_per_semester=1200 if room_number % 2 == 0 else 900,
                        building_number=building.building_number,
                        is_vacant=vacant_data,
                        max_count=2 if room_number % 2 == 0 else 3,
                        occupants=occupants_data)
            room.save()
