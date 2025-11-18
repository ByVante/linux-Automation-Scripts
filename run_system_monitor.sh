#!/bin/bash
# run_system_monitor.sh - Run system monitor and log output

cd "$(dirname "$0")"
source .venv/bin/activate
python system_monitor.py >> system_monitor_cron.log 2>&1
