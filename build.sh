#!/bin/bash

echo "Updating pip..."
python -m pip install -U pip

# Install dependencies
echo "Installing project dependencies..."
python -m pip install -r requirements.txt

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput --clear --output staticfiles_build
