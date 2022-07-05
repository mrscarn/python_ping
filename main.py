import subprocess
import platform

print ("PING SCANNER")

#Use different param depending if it's linux or windows
param = '-n' if platform.system().lower()=='windows' else '-c'

#Ping function
def ping(host):
    command = ["ping", param, "1", host]
    return subprocess.call(command, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT) == 0

#Create a single var for pinging single host
host = "google.com"

#If statement of wht the ping function returns
if ping(host):
    print("Ping successfull!")
else: 
    print("Ping unsuccessfull")
    
#Create a list of hosts for pinging    
host_list = ["google.com", "gt.se", "amazon.com"]

#For loop for printing and pinging a hosts in the previous host list
for host in host_list:
    print(host)
    ping(host)
    if ping(host):
        print("Ping successfull!")
    else: 
        print("Ping unsuccessfull")