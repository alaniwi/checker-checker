#!/bin/sh

[ -d venv ] || python -mvenv venv
. venv/bin/activate
which compliance-checker > /dev/null || pip install compliance-checker

if ! compliance-checker -l | grep -q wcrp_cmip7
then
    pip install cc-plugin-wcrp
    pip install esgvoc --upgrade
    esgvoc use cmip7@latest universe@latest
fi

