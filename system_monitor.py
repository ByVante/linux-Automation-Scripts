import psutil

# CPU usage
cpu = psutil.cpu_percent(interval=1)
print(f"CPU Usage: {cpu}%")

# Memory usage
memory = psutil.virtual_memory()
print(f"Memory Usage: {memory.percent}%")

# Disk usage
disk = psutil.disk_usage('/')
print(f"Disk Usage: {disk.percent}%")