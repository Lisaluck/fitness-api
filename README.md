Fitness Studio Booking API - README
📌 Introduction
This is a Fitness Studio Booking API built with Django REST Framework that provides a booking system for classes like Yoga, Zumba, and HIIT.

🚀 Features
View list of fitness classes

Book a class

View your bookings

Timezone support (default: IST)

SQLite database (for development)

⚙️ Setup Instructions
Prerequisites
Python 3.8+

Django 4.2+

SQLite (included with Python)

Installation
Clone the repository:
git clone https://github.com/yourusername/fitness-api.git
cd fitness-api
pip install -r requirements.txt
Run migrations:
python manage.py migrate
python manage.py seed_data
Start development server:
python manage.py runserver
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'fitness_db',
        'USER': 'youruser',
        'PASSWORD': 'yourpassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
🌐 API Endpoints
1. GET /api/classes/
List all upcoming fitness classes.

2. POST /api/book/
Book a class slot.

Request Body:

json
{
    "fitness_class": 1,
    "client_name": "lucky",
    "client_email": "lucky@example.com"
}
Example:
3. GET /api/bookings/
Get all bookings for a client.

Query Parameters:

email - Client email (required)

Example:
get "http://127.0.0.1:8000/api/bookings/?email=lucky@example.com"
