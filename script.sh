#!/bin/bash
set -e

echo "=== Starting IoT Project Deployment ==="
cd /app

mkdir -p staticfiles
mkdir -p data

echo "=== Running migrations ==="
python manage.py migrate --noinput

echo "=== Collecting static files ==="
python manage.py collectstatic --noinput --clear

echo "=== Starting Gunicorn server ==="
exec gunicorn iot.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 2 \
    --timeout 120 \
    --log-level info \
    --access-logfile - \
    --error-logfile - \
    --capture-output
