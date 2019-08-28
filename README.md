# fullstack-python

Simple CRUD API and complete basic django tutorial. It contains two project one is `mysite` and other is `hellodjango` both are independent app

### Steps for running hellodjango 

```sh
$ source training_django/bin/activate
$ cd hellodjango
$ python manage.py runserver
```

### Steps for running mysite 

```sh
$ cd mysite
$ pip install mysqlclient
$ pip install django
$ pip install django-rest-framework

In mysite/settings.py file change  `/etc/mysql/my.cnf` to your database config file 

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': '/etc/mysql/my.cnf',
        },
    }
}


```


