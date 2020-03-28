#!/bin/bash

kill -9 `ps aux | grep flask | grep -v grep | awk '{ print $2 }'`