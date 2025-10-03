#!/bin/sh

set -e
echo "Starting IoT Project Deployment..."

echo "Making migrations..."
python3 manage.py makemigrations

echo "Running migrations..."
python3 manage.py migrate

echo "Creating superuser if needed..."
python3 manage.py shell -c "
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@iot.com', 'admin123')
    print('Superuser created: admin/admin123')
else:
    print('Superuser already exists')
"

echo "Collecting static files..."
python3 manage.py collectstatic --noinput

echo "Starting Gunicorn server..."
exec gunicorn iot.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 2 \
    --timeout 30 \
    --log-level info \
    --access-logfile - \
    --error-logfile -
