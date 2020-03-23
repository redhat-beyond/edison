#!/bin/bash

time=`TZ=Asia/Jerusalem date '+%Y%m%d_%H%M'`
VAG_COMMON_DIR="/vagrant"
HOME="/home/vagrant"
LOG_DIR="$VAG_COMMON_DIR/log"
OUTFILE="$LOG_DIR/${time}_vagrant-out.log"
FLASK_APP_PY="$VAG_COMMON_DIR/flask_init.py"
FLASK_EXEC="$HOME/runFlask.sh"
FLASK_LOG="$LOG_DIR/flask-out.log"
KILLFLASK_SCRIPT="$VAG_COMMON_DIR/killFlask.sh"
FLASK_ONBOOT=false # Currently Flask On Startup feature disabled [ Not Supported ]

runSetup() {
    step=1

    if [ ! -d $LOG_DIR ]; then
        mkdir $LOG_DIR
    else
        # Deleting all vagrant-out log files except for the 5 most recent
        cd $LOG_DIR
        ls -t | grep vagrant-out.log$ | tail -n +6 | xargs -d '\n' -r rm --
        cd $HOME
    fi
    touch $OUTFILE

    if [ ! -e $FLASK_LOG ]; then
        touch $FLASK_LOG
    fi

    if [ ! -e $FLASK_APP_PY ]; then
        echo "ERROR: Missing $FLASK_APP_PY file..." >> $OUTFILE
        exit 1
    else
        chmod +x $FLASK_APP_PY
    fi

    # Adding execution permission to $KILLFLASK_SCRIPT 
    if [ -e $KILLFLASK_SCRIPT ]; then
        chmod +x $KILLFLASK_SCRIPT
    fi

    echo " "
    echo " "
    echo "==> Running Provision Script: $0:"
    echo " "
    echo "$((step++)). Installing Python PIP3..."
    sudo apt-get -yq update >> $OUTFILE 2>&1
    sudo apt-get -yq install python3-pip >> $OUTFILE 2>&1
    echo ""
    echo "$((step++)). Installing Flask..."
    sudo pip3 install Flask >> $OUTFILE 2>&1

    # Set Flask Run On Starup:
    if [ $FLASK_ONBOOT == true ] && [ -e $FLASK_EXEC ]; then
        echo "@reboot $FLASK_EXEC >> /dev/null 2>&1 &" > temp_cron
        crontab temp_cron
        rm temp_cron
    fi
    echo " "
    echo "$((step++)). Initiating Flask Server..."
    export FLASK_APP=$FLASK_APP_PY 
    flask run --host=0.0.0.0 >> $FLASK_LOG 2>&1 &
    echo " "
    
    exit 0
}

(runSetup)
if [ $? -eq 0 ]; then
    echo "Vagrant Completed Successfully!!!"
    exit 0
else
    echo "Vagrant Failed! Please see log file under $LOG_DIR"
    exit 1
fi
