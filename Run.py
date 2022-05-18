# This is where to call the methods defined in Definitions.py
from Definitions import *

# Target name and IP/address
targets = {
    "Google": "www.Google.com"
}

# Create a file called ips.txt and add name/ips there with a space delimiter
with open('ips.txt','r') as f:
    for line in f:
        nameIP = line.split()
        targets[nameIP[0]] = nameIP[1]

inputTime = input("Input Time in seconds.")

# input time in (even int)seconds to run and targets
loopPing(inputTime,targets)