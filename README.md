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

### 4. `network_diagnostics.py`
- Pings a list of hosts to check network reachability.
- Displays latency (ping time) for reachable hosts.
- Logs all results with timestamps in `network_diagnostics.log`.
- Run with:
  ```bash
  python network_diagnostics.py
