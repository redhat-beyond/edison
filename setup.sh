#!/bin/bash
time=`date '+%Y%m%d_%H%M'`
VAG_COMMON_DIR="/vagrant/"
LOG_DIR="$VAG_COMMON_DIR/log"
OUTFILE="$LOG_DIR/${time}_vagrant-out.log"
FLASK_APP_BODY="flask_init.txt"
FLASK_APP="/home/vagrant/hello.py"

runSetup() {
    step=1

    if [ ! -d $LOG_DIR ]; then
        mkdir $LOG_DIR
    fi

    if [ ! -e $OUTFILE ]; then
        touch $OUTFILE
    fi

    echo " "
    echo " "
    echo "==> Running Provision Script: $0:"
    echo " "
    echo "$((step++)). Updating apt-git repositories..."
    sudo apt-get update  >> $OUTFILE 2>&1 
    [ $? -ne 0 ] && exit 1
    sudo apt-get -yq install software-properties-common >> $OUTFILE 2>&1 
    [ $? -ne 0 ] && exit 1
    echo " "

    echo "$((step++)). Installing Python & PIP..."
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py  >> $OUTFILE 2>&1 
    [ $? -ne 0 ] && exit 1

    /usr/bin/python3 get-pip.py  >> $OUTFILE 2>&1 
    [ $? -ne 0 ] && exit 1

    sudo DEBIAN_FRONTEND=noninteractive apt-get -yq install python3-dev python3-pip  >> $OUTFILE 2>&1 
    [ $? -ne 0 ] && exit 1

    pip install --upgrade pip >> $OUTFILE 2>&1 
    echo " "

    echo "$((step++)). Installing Flask..."
    pip install flask  >> $OUTFILE 2>&1 
    [ $? -ne 0 ] && exit 1

    touch $FLASK_APP
    cat /$VAG_COMMON_DIR/$FLASK_APP_BODY > $FLASK_APP 
    # Enabling auto run of Flask on reboot
    chmod -x $FLASK_APP
    echo "@reboot nohup /usr/bin/python3 $FLASK_APP >> /dev/null 2>&1 &" > temp_cron
    crontab temp_cron
    rm temp_cron
    # Making a Script to enable killing Flask process ran by hello.py
    echo $'kill -9 `ps aux | grep hello.py | grep -v grep | awk \'{ print $2 }\'`' > killFlask.sh
    chmod +x killFlask.sh
    echo " "

    echo "$((step++)). Initiating Flask..."
    nohup /usr/bin/python3 $FLASK_APP >> /dev/null 2>&1 &
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
