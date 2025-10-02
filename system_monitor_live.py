import psutil
import time
import os

def clear_screen():
    # Works on Mac/Linux ('clear') and Windows ('cls')
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    clear_screen()
    
    # CPU usage
    cpu = psutil.cpu_percent(interval=1)
    # Memory usage
    memory = psutil.virtual_memory()
    # Disk usage
    disk = psutil.disk_usage('/')
    
    print("=== Live System Monitor ===")
    print(f"CPU Usage: {cpu}%")
    print(f"Memory Usage: {memory.percent}%")
    print(f"Disk Usage: {disk.percent}%")
    
    # Wait 5 seconds before refreshing
    time.sleep(5)
