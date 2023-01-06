#!/bin/sh

# Initalizing the DB
if $INITIALIZE_DB = true; then
    echo "Initializing Database"
    aerich init -t app.core.config.TORTOISE_ORM
    aerich init-db
fi

# Migrating the DB
if $MIGRATE_DB = true; then
    echo "Migrating Database"
    aerich migrate
    aerich upgrade
fi

sleep 5s

exec "$@"