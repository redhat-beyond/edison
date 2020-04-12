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

echo "running flask_init.py"
export FLASK_APP=/vagrant/flask_init.py
python3 -m flask run --host=0.0.0.0 >> /vagrant/log.log 2>&1 &
