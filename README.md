# 3megawatt company test
The task is to develop an application as shown on http://applicationtask.herokuapp.com. The requirements are as follow:

- Django as web framework
- Bootstrap as front-end framework
- Keep the URL logic
- Regarding the aggregations: please implement one in Python code and the other one as database query, using Django's database API over raw SQL.
# Table of Contents

* [Requirement](#requirement)
* [Django Installation](#installation)
* [Python code](#python_code)

<a name="requirement"></a>
### Requirement:
* Django==2.0.6
* Python 3.6.1

<a name="installation"></a>
### Installation:
Following Step need to follow:
1. Git clone this code at your system
2. pip install -r requirements.txt
3. Run the migration ``` python manae.py migrate ```
4. Create admin users
``` python manage.py createsuperuser```
5. Run the application by: ```python manage.py runserver```
6. Login to admin section by /admin
7. Go to Sites and add some sites and the value for each sites

Now you can see the changes on front-end
Note: As per the requirement mention I used raw SQL.

<a name="python_code"></a>
### Python code:
As per the point no. 4 (Regarding the aggregations) one i have to develop in python.
So, You can test python with the same database
1. Open the terminal on same application.
2. Run the command ```python core_python.py```

Here you can see the Site list and there sum and average value.

