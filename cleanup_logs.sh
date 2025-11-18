#!/bin/bash
# cleanup_logs.sh - Delete log files older than 7 days in /var/log

LOG_DIR="/var/log"
DAYS=7

echo "🧹 Cleaning up logs in $LOG_DIR older than $DAYS days..."

find "$LOG_DIR" -name "*.log" -type f -mtime +$DAYS -exec rm -v {} \;

echo "✅ Cleanup complete."
