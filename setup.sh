#!/bin/bash

FLASK_SERVE_STATIC_PORT=5000
FLASK_RESTFUL_PORT=3000

echo "updating apt before installation"
sudo apt-get update

echo "installing python 3.7"
sudo apt-get install -y python3.7 

echo "installing python3-pip"
sudo apt-get install -y python3-pip

echo "installing PostgreSQL"
sudo apt-get install -y postgresql postgresql-contrib

echo "install requirements"
pip3 install -r /vagrant/requirements.txt

echo "configuring database"
sudo su postgres <<POSTGRESQL_COMMANDS
psql
CREATE DATABASE edison;
ALTER ROLE postgres WITH PASSWORD 'edison';
POSTGRESQL_COMMANDS

export FLASK_ENV=development

echo "running flask_serve_static.py"
export FLASK_APP=/vagrant/flask_serve_static.py
flask run -h 0.0.0.0 -p $FLASK_SERVE_STATIC_PORT >> /vagrant/flask_serve_static.log 2>&1 &

echo "running flask_restful_api.py"
export FLASK_APP=/vagrant/backend/flask_restful_api.py
flask run -h 0.0.0.0 -p $FLASK_RESTFUL_PORT >> /vagrant/flask_restful_api.log 2>&1 &
