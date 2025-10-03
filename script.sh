#!/bin/bash
set -e

echo "=== Starting IoT Project Deployment ==="

echo "=== Running migrations ==="
python3 manage.py migrate --noinput || true

echo "=== Collecting static files ==="
python3 manage.py collectstatic --noinput || true

echo "=== Starting Gunicorn server ==="
exec gunicorn iot.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 2 \
    --timeout 120 \
    --log-level debug \
    --access-logfile - \
    --error-logfile - \
    --capture-output
