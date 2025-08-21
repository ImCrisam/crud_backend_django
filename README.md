# CRUD Backend Django (Brands)

This is a minimal Django project that exposes a REST CRUD for `Brand` records.

Quick notes:

- The project uses Django and Django REST Framework (DRF).
- There's a fake middleware `brands.middleware.FakeAuthMiddleware` that attaches a
  `request.fake_user` dict and sets `X-FAKE-AUTH` header for local development.
- By default the project uses SQLite. To run with Postgres using Docker, see below.

Run locally (sqlite):

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Run with docker-compose (Postgres):

```bash
# start DB
docker compose up -d
# set env and run migrations (example using bash)
export POSTGRES_DB=cruddb
export POSTGRES_USER=cruduser
export POSTGRES_PASSWORD=crudpass
export POSTGRES_HOST=localhost
export POSTGRES_PORT=5432
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

API endpoints:

- `GET /api/brands/` list brands
- `POST /api/brands/` create brand (name, description)
- `GET /api/brands/{id}/` retrieve
- `PUT/PATCH /api/brands/{id}/` update
- `DELETE /api/brands/{id}/` delete

Notes:
- The `FakeAuthMiddleware` is intentionally simple. Remove it from
  `MIDDLEWARE` in `settings.py` before deploying to production.
