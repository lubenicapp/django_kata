# Django kata, just for practice


## specs

Create an api that expose `customers/` `customers/<id>`

allow filter query param on `last_name` : `customers?last_name=Offin`


Allo `PUT` method only if an Authorization header is provided `Authorization: Magic_Key` (hard coded)

Apply data validation on `age > 18` for `PUT`


## Run the project

in `./web` rename `sample.env` as `.env`

run `docker-compose up`

and visit
- `localhost:8000/api/customers`
- `localhost:8000/api/customers/6`, submit a PUT request with the form
- `localhost:8000/api/customers/age/average`
