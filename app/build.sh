#!/bin/bash
pip install djangorestframework &&
python /app/mmk2nh_cs4501/manage.py makemigrations helloworld &&
python /app/mmk2nh_cs4501/manage.py migrate helloworld &&
python /app/mmk2nh_cs4501/manage.py loaddata /app/mmk2nh_cs4501/db.json &&
mod_wsgi-express start-server --reload-on-changes --working-directory /app/mmk2nh_cs4501 /app/mmk2nh_cs4501/mmk2nh_cs4501/wsgi.py