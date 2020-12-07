![Python package](https://github.com/beebus/crispy-spoon/workflows/Python%20package/badge.svg?branch=master)
# crispy-spoon
flask playground based on https://www.linkedin.com/learning/learning-flask-2

```
$ heroku login
```
heroku: Press any key to open up the browser to login or q to exit:<br>
Opening browser to https://cli-auth.heroku.com/auth/browser/...<br>
Logging in... done<br>
Logged in as...<br>
```
$ heroku create
```
Creating app... done, [appname]...<br>
```
$ heroku addons:create heroku-postgresql:hobby-dev -a [appname]
```
Creating heroku-postgresql:hobby-dev on [appname]... free<br>
Database has been created and is available<br>
 ! This database is empty. If upgrading, you can transfer<br>
 ! data from another database with pg:copy<br>
Created postgresql-something-37746 as DATABASE_URL<br>
Use heroku addons:docs heroku-postgresql to view documentation<br>
```
$ heroku config -a [appname]
```
(Save the response info)
```
$ sudo pip install --upgrade pip
$ sudo pip install virtualenv
```


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
