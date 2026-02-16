# Iftar Locations API

This Django REST Framework project provides an API to list and query Iftar locations in Algeria. Users can retrieve the nearest locations by latitude and longitude.

---

## 1. Project Setup

### 1.1 Clone the Repository

```bash
git clone <your-repo-url>
cd iftar_backend

1.2 Create a Virtual Environment and Activate It
python3 -m venv venv
source venv/bin/activate
```

1.3 Install Dependencies

Create a requirements.txt file with the following content:

Django==6.0.2
djangorestframework==3.16.1
django-filter==25.2
psycopg2-binary==2.9.11
numpy==1.26.4


Install dependencies:

pip install -r requirements.txt

1.4 Database Setup (PostgreSQL + PostGIS)

Install PostgreSQL and PostGIS:

sudo apt update
sudo apt install postgresql postgresql-contrib postgis postgresql-15-postgis-3


Create database and user:

sudo -u postgres psql


Inside the psql shell:

-- Create a new database
CREATE DATABASE iftar_db;

-- Create a user
CREATE USER iftar_user WITH PASSWORD 'yourpassword';

-- Grant privileges
GRANT ALL PRIVILEGES ON DATABASE iftar_db TO iftar_user;

-- Connect to your database
\c iftar_db

-- Enable PostGIS extension
CREATE EXTENSION postgis;

-- Verify PostGIS installation
SELECT PostGIS_Version();


Update settings.py DATABASES section:

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'iftar_db',
        'USER': 'iftar_user',
        'PASSWORD': 'yourpassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


Run migrations:

python manage.py makemigrations
python manage.py migrate

2. Admin Setup
2.1 Create a Superuser
python manage.py createsuperuser


Access Django admin at:

http://127.0.0.1:8000/admin/

2.2 Register Iftar Locations in Admin
from django.contrib import admin
from .models import IftarLocation

@admin.register(IftarLocation)
class IftarLocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'address', 'is_active', 'created_at')


Note: The map widget is disabled, so you can only input latitude/longitude manually.

3. API Usage
3.1 Nearest Locations
GET http://127.0.0.1:8000/api/iftar/nearest/?lat=<latitude>&lng=<longitude>

3.2 Pagination

Configured to return 15 locations per page:

# settings.py
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 15
}

4. Run Server
python manage.py runserver


API will be available at:

http://127.0.0.1:8000/api/iftar/nearest/?lat=36.7525&lng=3.0420

5. Adding Locations

Use the admin interface to add new locations. Provide:

Name

City

Address

Latitude

Longitude

Active status

6. Notes

Make sure django-filter is installed, or API filtering will fail.

PostgreSQL must have PostGIS enabled if you plan to use geospatial queries.

This project is designed for Algeria Iftar locations, but can be extended
