```bash
django-admin startproject main .
python manage.py startapp registration
python manage.py startapp api
python manage.py migrate
# password: Administrator
python manage.py createsuperuser --email notexist@qq.com --username admin
```