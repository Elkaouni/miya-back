
```shell
cd C:\Users\wichy\Desktop\MyProjects\MIYA-Personal-Assistant\miya\miya-webapp\django-back
pip install pipenv
pipenv install django
```
After installing django in the virtual env, i notice two files were added to the directory. Now, i need to start that empty env
```shell
pipenv shell
```
To view all the commands i can do with django use ``` django-admin ```

Start a new django project in the current directory:
```shell
django-admin startproject miyabackv1 .
```

To run the app:
```shell
python manage.py runserver
```

