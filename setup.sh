#!/bin/bash
time=`TZ=Asia/Jerusalem date '+%Y%m%d_%H%M'`
VAG_COMMON_DIR="/vagrant"
HOME="/home/vagrant"
LOG_DIR="$VAG_COMMON_DIR/log"
OUTFILE="$LOG_DIR/${time}_vagrant-out.log"
FLASK_APP_PY="$VAG_COMMON_DIR/flask_init.py"
FLASK_DIR="$HOME/FlaskApp"
FLASK_EXEC="$HOME/runFlask.sh"
KILLFLASK_SCRIPT="$VAG_COMMON_DIR/killFlask.sh"
PYTHON3="`which python3`"
FLASK_ONBOOT=false # Currently Flask On Startup feature disabled [ Not Supported ]

runSetup() {
    step=1

    if [ ! -e $FLASK_APP_PY ]; then
        echo "ERROR: Missing $FLASK_APP_PY file..." >> $OUTFILE
        exit 1
    else
        chmod +x $FLASK_APP_PY
    fi

    if [ ! -d $FLASK_DIR ]; then
        mkdir $FLASK_DIR
    fi

    if [ ! -d $LOG_DIR ]; then
        mkdir $LOG_DIR
    else
        rm -f $LOG_DIR/*vagrant-out.log
    fi
    touch $OUTFILE
    # Adding execution permission to $KILLFLASK_SCRIPT 
    if [ -e $KILLFLASK_SCRIPT ]; then
        chmod +x $KILLFLASK_SCRIPT
    fi

    echo " "
    echo " "
    echo "==> Running Provision Script: $0:"
    echo " "
    echo "$((step++)). Installing & Activating Python-3 Virtual Environment..."
    sudo apt-get install -yq python3-venv >> $OUTFILE 2>&1 
    cd $FLASK_DIR
    $PYTHON3 -m venv venv
    source venv/bin/activate
    echo " "
    echo "$((step++)). Installing Flask..."
    pip install Flask >> $OUTFILE 2>&1

    # Set Flask Run On Starup:
    if [ $FLASK_ONBOOT == true ] && [ -e $FLASK_EXEC ]; then
        echo "@reboot $FLASK_EXEC >> /dev/null 2>&1 &" > temp_cron
        crontab temp_cron
        rm temp_cron
    fi
    echo " "
    echo "$((step++)). Initiating Flask Server..."
    export FLASK_APP=$FLASK_APP_PY 
    flask run --host=0.0.0.0 >> /dev/null 2>&1 &
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
