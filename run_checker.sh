#!/bin/sh

. venv/bin/activate
. ./paths.sh

python run_checker.py good:$good_path warn:$warn_path fail:$fail_path 
