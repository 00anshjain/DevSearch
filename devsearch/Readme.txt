#This admin panel cannot be accessed until we have our database ready.
SO we need to run command and bulid out tables

python manage.py migrate

This isbecause we are making tables first time
From now onwards we will have to run makemigrations and then migrate

Now we can runserver again and try going to admin panel
admin panel is simple a way to access the database

Django gives us admin panelthat we can use to access our data, modify and so onwards

Before we get started we do need a user to login

So we run command ->  python manage.py createsuperuser
By default it will give username as that of pc

We can perform crud operations from the admin panel i.e.
create, update and delete.