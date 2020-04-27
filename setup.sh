#!/bin/bash

FLASK_PORT=5000

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
sudo -u postgres createdb edison
sudo -u postgres psql -c "ALTER ROLE postgres WITH PASSWORD 'edison';"

export FLASK_ENV=development

echo "running app.py"
export FLASK_APP=/vagrant/edison/app.py
flask run -h 0.0.0.0 -p $FLASK_PORT >> /vagrant/edison/app.log 2>&1 &
