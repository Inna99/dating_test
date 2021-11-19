# dating_test
backend for a dating site.

### To start, follow these steps

- pip install -r requirements.txt
- docker run --name postgres -e POSTGRES_PASSWORD=postgres -d -p 5432:5432 postgres
- docker start postgres
- cd django_sms
- ./migrate.sh
- python manage.py runserver