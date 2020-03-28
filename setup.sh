#!/bin/bash

echo "updating apt before installation"
sudo apt update

echo "installing python 3.7"
sudo apt install -y python3.7 

echo "installing python3-pip"
sudo apt install -y python3-pip
pip3 install --upgrade pip

echo "installing flask"
#'python3 -m' was added to avoid warnings
python3 -m pip install flask

echo "running flask_init.py"
FLASK_APP=/vagrant/flask_init.py flask run --host=0.0.0.0 >> /vagrant/log.log 2>&1 &
