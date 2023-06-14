# CRUD-Application
This blog CRUD application simplifies the process of managing and organizing blog entries for the purposes of creating, reading, updating, and deleting.
### Technologies used
***
* Django
* DRF


### Installation
***
```
$ git clone https://github.com/jobayer-rahman/CRUD-Application.git
$ cd CRUD-Application
$ python3 -m venv venv
$ source venv/bin/activate                   (for Unix or MacOS)
$ venv\Scripts\activate.bat                  (for windows)
$ pip install -r requirements.txt
$ python manage.py migrate
$ python manage.py runserver
```

### API Urls
```
$ http://127.0.0.1:8000/author/
$ http://127.0.0.1:8000/post/
$ http://127.0.0.1:8000/comment/
$ http://127.0.0.1:8000/documentation/
```