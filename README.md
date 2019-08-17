# crispy-spoon
flask playground

In a folder with a .py file and a requirements.txt file, run the following.
```
$ virtualenv venv
```
Using base prefix '/usr'... Installing setuptools, pip, wheel...<br>
done.
```
$ source venv/bin/activate
$ pip install -r requirements.txt
$ export FLASK_APP=flask-basic.py
$ flask run
```
 * Serving Flask app "flask-basic"
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)<br>
127.0.0.1 - - [17/Aug/2019 03:12:39] "GET / HTTP/1.1" 200 -<br>
127.0.0.1 - - [17/Aug/2019 03:12:39] "GET /favicon.ico HTTP/1.1" 404 -
