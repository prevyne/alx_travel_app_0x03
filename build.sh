#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

# Use the correct path to manage.py
python alx_travel_app/manage.py collectstatic --no-input
python alx_travel_app/manage.py migrate
