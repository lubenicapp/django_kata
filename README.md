# Django kata, just for practice


## specs

Create an api that expose `customers/` `customers/<id>`

allow filter query param on `last_name` : `customers?last_name=Offin`


Allo `PUT` method only if an Authorization header is provided `Authorization: Magic_Key` (hard coded)

Apply data validation on `age > 18` for `PUT`


## Run the project

open a terminal in ./integration and run `docker-compose up`

in another terminal in the root of the project run `python manage.py migrate --fake api`
(fake because we already created the table setting up the db)
then `python manage.py migrate`

rename `.env` as `sample.env` and eventually change the host as "localhost". depend on your docker config


then `python manage.py runserver`

and visit `localhost:8000/api/customers`
