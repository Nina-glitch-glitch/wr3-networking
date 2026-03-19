# Work Requirement 3 – Networking (Socket Task)
import socket
# Hostname to resolve
hostname = "vg.no"
# Get IP address from hostname
ip_address = socket.gethostbyname(hostname)
# Print result
print(f"Hello! The IP address of {hostname} is {ip_address}")
# Testing others and lokal machine
local_machine = socket.gethostname()
websites = ["nrk.no", "google.com", local_machine]
# Loop for testing
for site in websites:
    ip = socket.gethostbyname(site)
    print(f"{site} : {ip}")
