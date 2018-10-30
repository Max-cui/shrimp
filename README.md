# init Shrimp Project

start server
python manager.py runserver

indes page
http://localhost:8000

admin console
http://localhost:8000/admin

init database tables
python manage.py makemigrations
python manage.py migrate

create admin user
python manage.py createsuperuser
