import subprocess
import platform
from datetime import datetime

print("=== Network Diagnostics ===")

# Detect OS for correct ping syntax
param = "-n" if platform.system().lower() == "windows" else "-c"

# Read the hosts file
try:
    with open("hosts.txt", "r") as f:
        hosts = [line.strip() for line in f.readlines() if line.strip()]
except FileNotFoundError:
    print("❌ hosts.txt file not found.")
    exit(1)

# Make sure we have hosts to test
if not hosts:
    print("❌ No hosts found in hosts.txt.")
    exit(1)

log_file = "network_diagnostics.log"

# Loop through each host
for host in hosts:
    try:
        print(f"Pinging {host}...")  # Debug line
        result = subprocess.run(
            ["ping", param, "1", host],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        if result.returncode == 0:
            # Extract latency
            if "time=" in result.stdout:
                start = result.stdout.find("time=")
                time_info = result.stdout[start:].split(" ")[0]
                status = f"✅ {host} is reachable ({time_info})"
            else:
                status = f"✅ {host} is reachable"
        else:
            status = f"❌ {host} is unreachable"

    except Exception as e:
        status = f"⚠️ Error checking {host}: {e}"

    # Print and log
    print(status)
    with open(log_file, "a") as log:
        log.write(f"[{datetime.now()}] {status}\n")

print("\nDiagnostics complete. Results saved to network_diagnostics.log ✅")
