Uber Mapper
=======

Unfortunately, Uber have since removed the historical data endpoint, so this project no longer works, will update if ever this endpoint returns.


Setup
----------------

**Setup database**

    $ python manage.py syncdb
    

**Configure API Keys**

Create a new app at https://developer.uber.com/

Open uber_mapper/settings.py and set the configuration variables with the keys you are provided:

UBER_CLIENT_ID = 'xxx'

UBER_CLIENT_SECRET = 'xxx'

UBER_APP_NAME = 'AppName'

UBER_REDIRECT_URI = 'http://localhost:8000/login_return'


**Run app**

    $ python manage.py runserver
