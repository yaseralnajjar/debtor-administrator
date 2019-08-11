## Debtor Administration

A simple app  manage (CRUD) debtors, their bank account data (IBAN) and invoices.

## Existing Models and APIs

The [models.txt file](./docs/models.txt) and the [api.txt file](./docs/api.txt) contains all the models and the APIs that we have in the app, respectively.

Both of the models and the APIs are built upon the [wireframe file](./docs/wireframe.jpg)

## Setup

```
yarn install
virtualenv venv
call venv\Scripts\activate
pip install -r requirements_dev.txt
python manage.py migrate
```

## Running Development Servers

```
python manage.py runserver
```

From another tab in the same directory:

```
yarn serve
```

The Vuejs application will be served from `localhost:8080` and the Django Api
and static files will be served from `localhost:8000`.

## Docker Support

To run the app using Docker just add `127.0.0.1 debtor.admin` into your hosts file (in system32/drivers/etc folder).

After that, add your `.env` file similar to [sample.env file](./sample.env)

Then you're ready to launch your development containers:

```
docker-compose -f docker-compose-dev.yml up -d
```

For staging containers:

```
docker-compose -f docker-compose.yml -f docker-compose-staging.yml up -d
```

You will find the app on [http://debtor.admin](http://debtor.admin)

## Deploy Guide

You can use the "one-click deploy" button below to try it out on Heroku, but you would still to do the following:

1. Add admin user

Simply by running these commands, you will get an admin account with "admin" password.

> DONT FORGET TO CHANGE PASSWORD LATER

```
heroku git-remote -a YOUR_APP_NAME
heroku run python manage.py shell
from django.contrib.auth.models import User
User.objects.create_superuser('admin', 'admin@example.com', 'admin')
```

2. Adding Social App

You need to add your Google OAuth credentials to the app through the Django admin.

3. ENJOY!


##### Heroku One Click Deploy

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/yaseralnajjar/debtor-administrator)
