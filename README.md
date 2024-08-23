# FastAPI + SQLModel + Alembic

Sample FastAPI project that uses async SQLAlchemy, SQLModel, Postgres, Alembic, and Docker.

## Want to learn how to build this?

Check out the [post](https://testdriven.io/blog/fastapi-sqlmodel/).

## Want to use this project?

```sh
$ docker-compose up -d --build
$ docker-compose exec web alembic upgrade head
```

Sanity check: [http://localhost:8004/ping](http://localhost:8004/ping)

Add a song:

```sh
$ curl -d '{"name":"Midnight Fit", "artist":"Mogwai", "year":"2021"}' -H "Content-Type: application/json" -X POST http://localhost:8004/songs
```

Get all songs: [http://localhost:8004/songs](http://localhost:8004/songs)


# Open psql:
docker-compose exec db psql --username=postgres --dbname=foo
\dt

# Migrations
Create:
docker-compose exec web alembic revision --autogenerate -m "commit message"

Run:
docker-compose exec web alembic upgrade head

# Documentation
docker run --rm --network fastapi-sqlmodel-alembic_default -v ${PWD}:/work -w /work k1low/tbls doc postgresql://postgres:postgres@db:5432/foo?sslmode=disable


# ToDos
23.08:
- Create Colors & initial UserQuestion with Script
- getting UserQuestion, is answerSet returned?
- create UserQuestion Models & Endpoint
- create UserData Models & Endpoint
- get UserData Models & Endpoint
...
- Auth:
    - Tables
    - Library
    - Login ermöglichen & Überlegen
--> Frontend!
