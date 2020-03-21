#!/bin/bash

#FLASK_APP_FILE="flask_init.py"
#kill -9 `ps aux | grep $FLASK_APP_FILE | grep -v grep | awk '{ print $2 }'`

kill -9 `ps aux | grep flask | grep -v grep | awk '{ print $2 }'`