#!/bin/bash

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
