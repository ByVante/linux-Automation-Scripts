# Linux Automation Scripts

A collection of beginner-friendly automation scripts for Linux system monitoring and operations, written in **Python** and **Bash**.  
These scripts demonstrate practical skills in automation, monitoring, and basic DevOps practices.

---

## 📂 Scripts

### 1. `system_monitor.py`
- Takes a one-time snapshot of:
  - CPU usage
  - Memory usage
  - Disk usage
- Run with:
  ```bash
  python system_monitor.py
  ```

---

### 2. `cleanup_logs.sh`
- A **Bash script** that finds and deletes log files older than **7 days** in `/var/log`.
- Useful for keeping systems tidy and preventing old logs from consuming disk space.
- Run with:
  ```bash
  chmod +x cleanup_logs.sh
  ./cleanup_logs.sh
  ```

---

### 3. `website_checker.py`
- Checks if a list of websites are reachable.
- Uses HTTP requests with error handling.
- Prints status for each website:
  - ✅ UP (site is reachable and responding)
  - ⚠️ Warning (site responds but with an error code)
  - ❌ DOWN (site is unreachable or times out)
- Run with:
  ```bash
  python website_checker.py
  ```

---

## 🚀 Future Improvements

- **Archiving logs instead of deleting**  
  Instead of permanently deleting logs, an enhancement could compress and archive them first for safer storage.  

  Example implementation:  
  ```bash
  #!/bin/bash
  # cleanup_logs.sh - Archive and clean log files older than 7 days in /var/log

  LOG_DIR="/var/log"
  DAYS=7
  ARCHIVE="old_logs_$(date +%Y%m%d).tar.gz"

  echo "🗄️ Archiving logs older than $DAYS days from $LOG_DIR into $ARCHIVE..."

  find "$LOG_DIR" -name "*.log" -type f -mtime +$DAYS -print0 | tar -czvf "$ARCHIVE" --null -T -

  echo "🧹 Deleting archived logs..."
  find "$LOG_DIR" -name "*.log" -type f -mtime +$DAYS -delete

  echo "✅ Cleanup and archive complete. Logs saved in $ARCHIVE."
  ```

---

## 📖 Purpose

This repository serves as a learning and showcase project to build confidence with:  
- Writing and running Python scripts for monitoring tasks  
- Automating system maintenance with Bash  
- Practicing version control with Git and GitHub  

These are small but practical projects that demonstrate technical growth and readiness to take on larger DevOps or automation challenges.
