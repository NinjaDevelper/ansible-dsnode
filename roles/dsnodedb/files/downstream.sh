#!/bin/bash

/home/dsnode/.env/bin/python /home/dsnode/downstream-node/runapp.py --cleandb >> /home/dsnode/cron.log 2>&1
