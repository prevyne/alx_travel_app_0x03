#!/usr/bin/env bash
# exit on error
# command to add execution permission to git: git update-index --chmod=+x build.sh

set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate