#! /usr/bin/env bash

# Let the DB start
python3 -m app.backend_pre_start

# Run migrations
alembic upgrade head

# Create initial data in DB
python3 -m app.initial_data
