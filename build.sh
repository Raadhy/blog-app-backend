#!/bin/bash

echo "Updating pip..."
python3.12 -m pip install -U pip

# Install dependencies
echo "Installing project dependencies..."
python3.12 -m pip install -r requirements.txt

# Collect static files
echo "Collecting static files..."
python3.12 manage.py collectstatic --noinput --clear staticfiles_build
