#!/bin/bash

VAG_COMMON_DIR="/vagrant"
LOG_DIR="$VAG_COMMON_DIR/log"
FLASK_APP_PY="$VAG_COMMON_DIR/flask_init.py"
FLASK_LOG="$LOG_DIR/flask-out.log"

export FLASK_APP=$FLASK_APP_PY 
flask run --host=0.0.0.0 >> $FLASK_LOG 2>&1 &