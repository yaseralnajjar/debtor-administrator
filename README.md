## Debtor Administration

A simple app  manage (CRUD) debtors, their bank account data (IBAN) and invoices.

## Setup

```
yarn install
virtualenv venv
call venv\Scripts\activate
pip install -r requirements.txt
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

##### Heroku One Click Deploy

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/yaseralnajjar/hackcyprus-hitup)
