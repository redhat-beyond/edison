#!/bin/bash

echo "updating apt before installation"
sudo apt update

echo "installing python 3.7"
sudo apt install -y python3.7 

echo "installing python3-pip"
sudo apt install -y python3-pip

echo "installing flask"
pip3 install flask

echo "installing flask restful"
pip3 install flask-restful

echo "installing flask jwt"
pip3 install flask-jwt-extended

echo "installing passlib"
pip3 install passlib

echo "installing flask-sqlalchemy"
pip3 install flask-sqlalchemy

echo "installing psycopg2-binary"
pip3 install psycopg2-binary

echo "installing postgresql"
sudo apt-get install -y postgresql postgresql-contrib

echo "configuring database"
sudo su postgres <<POSTGRESQL_COMMANDS
psql
CREATE DATABASE edison;
ALTER ROLE postgres WITH PASSWORD 'edison';
POSTGRESQL_COMMANDS

echo "running flask_init.py"
export FLASK_APP=/vagrant/flask_init.py
flask run -h 0.0.0.0 -p 5000 >> /vagrant/flask_init.log 2>&1 &

echo "running app.py"
export FLASK_APP=/vagrant/backend/app.py
flask run -h 0.0.0.0 -p 3000 >> /vagrant/app.log 2>&1 &