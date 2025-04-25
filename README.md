##  Health Information System – Backend

This is the backend of the Health Information System, built using **Django** and **Django REST Framework**. It allows doctors to manage clients and enroll them in health programs like TB, Malaria, HIV, etc.

##  Features

-  Register new clients
- Create health programs
-  Enroll clients into one or more health programs
-  Search and retrieve client profiles
-  Expose client data via a public REST API

##  Tech Stack

- [Django](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [SQLite](https://www.sqlite.org/index.html) (for development)

## 📦 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/JaneKahiu/health-system.git
cd health-system/health-system-backend
##Create & Activate Virtual Environment
  -python -m venv venv
##Install Dependencies
  -pip install -r requirements.txt
## Run Migrations
 -python manage.py makemigrations
-python manage.py migrate
## Run Development Server
-python manage.py runserver





