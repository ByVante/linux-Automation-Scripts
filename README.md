# Linux Automation Scripts

A collection of beginner-friendly automation scripts for Linux system monitoring and operations, written in Python.

## Scripts

### 1. `system_monitor.py`
- Takes a one-time snapshot of:
  - CPU usage
  - Memory usage
  - Disk usage
- Run with:
  ```bash
  python system_monitor.py

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
