import subprocess
import platform

print ("PING SCANNER")

#Sätt parameter n om Linux och c om Windows
param = '-n' if platform.system().lower()=='windows' else '-c'

#Ping function
def ping(host):
    command = ["ping", param, "1", host]
    return subprocess.call(command, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT) == 0

#Pinga enskild host
host = "google.com"

if ping(host):
    print("Ping successfull!")
else: 
    print("Ping unsuccessfull")
    
#En lista för hostar som ska pingas  
host_list = ["google.com", "gt.se", "amazon.com"]

#Loop som pingar varje host i listan
for host in host_list:
    print(host)
    ping(host)
    if ping(host):
        print("Ping successfull!")
    else: 
        print("Ping unsuccessfull")