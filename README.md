# project-management-system


##Overview
This repository contains the backend for the Project Management System, made with Django and REST.

##Setup Instructions

1. **Clone the repository:**
  ```bash
   git clone https://github.com/basak-tepe/project-management-system.git
   cd project-management-system
  ```

2. **Install PostgreSQL**

   Install PostgreSQL if not already installed. Create a new database.

3. **Configure Django Settings**

   Update the following DjangoAPI/settings.py file according to your credentials.

  ```python
   DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'testdb',
        'USER': 'testuser',
        'PASSWORD': 'testpassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
  }
 ```

4. **Apply migrations**
  ```bash
   python manage.py makemigrations ProjectApp
   python manage.py migrate ProjectApp
  ```

5. **Run the Development Server**
   
  ```bash
    python manage.py runserver
  ```

6. **Set up the Front-End**
   
  Follow the instructions [here](https://github.com/basak-tepe/project-management-ui/blob/main/README.md)
   
