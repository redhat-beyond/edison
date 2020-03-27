#!/bin/bash

echo "updating apt before installation"
sudo apt update

echo "installing python3-pip"
sudo apt install -y python3-pip
pip3 install --upgrade pip

echo "installing flask"
pip3 install flask

echo "running flask_init.py"
FLASK_APP=/vagrant/flask_init.py flask run --host=0.0.0.0
