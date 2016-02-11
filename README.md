# skeleton
A simple Django starter template

## Setup Instructions ##
1. Make sure you have Django-1.8.8 installed on your system
2. Create your new Django project by running this command

  `django-admin.py startproject mynewproject --template=https://github.com/kaizentech/skeleton/archive/master.zip`  
  
3. Install requirements by running this command from your project dir
  
  `pip install -r requirements.txt`

4. Setup these environment variables on your system (or in virtualenv)


On Windows
  
```
  set "DEBUG=True"
  set "DJANGO_SETTINGS_MODULE=config.settings.dev"
  set "SECRET_KEY=xxxxxYourxxSecretxxKeyxxxxx"
  set "DATABASE_URL=psql://username:password@127.0.0.1:5432/dbname"
```
  
  On Linux
  
```
  export DEBUG='TRUE'
  export DJANGO_SETTINGS_MODULE='config.settings.dev'
  export SECRET_KEY='xxxxxYourxxSecretxxKeyxxxxx'
  export DATABASE_URL='psql://username:password@127.0.0.1:5432/dbname'
```

You can also save these in your vurtualenv's script for auto invocation during virtualenv initialization 
  
5. Apply Migrations by running this command from the project dir
  
  `python manage.py migrate` 

6. Create Super User

  `python manage.py createsuperuser`

6. Finally run your dev server by running this command from your project dir
  
  `python manage.py runserver` 

# Goodies Included #
1. Seprate settings for development and production environment
2. Settings based on [django-environ](https://django-environ.readthedocs.org/en/latest/)
3. Excellent admin interface by [django-grappelli] (https://django-grappelli.readthedocs.org/en/latest/index.html)
4. Great Blogging app [django-blog-zinnia](https://github.com/Fantomas42/django-blog-zinnia)
