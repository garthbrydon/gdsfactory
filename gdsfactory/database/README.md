# Dev Env Setup

## First time setup

```bash
# setup envars
cp .env.local .env

# setup local database
alembic -c gdsfactory/database/migrations/alembic.ini upgrade head
```

## Database updates

```bash
alembic -c gdsfactory/database/migrations/alembic.ini revision --autogenerate "[description of your change]"
alembic -c gdsfactory/database/migrations/alembic.ini upgrade head
```

## DB CLI

Add wafer

```bash
 gf-db add_wafer "testwafer"
 ```
