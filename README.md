# django-localization-demo

**init environment**
+ sudo apt-get install python-dev
+ sudo apt-get install libmysqld-dev
+ sudo apt-get install python-pip
+ sudo pip install demo
+ vim ~/.bashrc

`source /usr/local/bin/virtualenvwrapper.sh`
+ source ~/.bashrc

**create virtualenv**
+ mkvirtualenv demo
+ workon demo
+ cd /path/to/demo
+ pip install -r requirements.txt
+ python manage.py migrate
+ python manage.py createsuperuser
+ python manage.py runserver


**makemessages**
+ sudo apt-get install gettext (if not install)
+ django-admin makemessages -a

**others**
+ [Poedit(windows)](https://poedit.net/)
+ [django-localization-demo](http://www.missuor.com/blog/2016/9/django-localization-demo)
