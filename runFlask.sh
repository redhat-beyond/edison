#!/bin/bash

VAG_COMMON_DIR="/vagrant"
HOME="/home/vagrant"
LOG_DIR="$VAG_COMMON_DIR/log"
FLASK_APP_PY="$VAG_COMMON_DIR/flask_init.py"
FLASK_DIR=$HOME/FlaskApp

cd $FLASK_DIR
if [ -e venv/bin/activate ]; then
    source venv/bin/activate
    export FLASK_APP=$FLASK_APP_PY 
    flask run --host=0.0.0.0 >> /dev/null 2>&1 &
fi
