import subprocess
import platform

print ("PING SCANNER")

param = '-n' if platform.system().lower()=='windows' else '-c'

def ping(host):
    command = ["ping", param, "1", host]
    return subprocess.call(command, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT) == 0

host = "google.com"

if ping(host):
    print("Ping successfull!")
else: 
    print("Ping unsuccessfull")
    
    
host_list = ["google.com", "gt.se", "amazon.com"]

for host in host_list:
    print(host)
    ping(host)
    if ping(host):
        print("Ping successfull!")
    else: 
        print("Ping unsuccessfull")