#! /usr/bin/env bash

# Let the DB start
python3 -m app.backend_pre_start

# Run migrations
aerich init -t app.core.config.TORTOISE_ORM

# Create initial data in DB
python3 -m app.initial_data
