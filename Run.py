# This is where to call the methods defined in Definitions.py
from Definitions import *

# Target name and IP/address
targets = {
    "Google": "www.Google.com",
    "Zay": "192.168.0.104",
    "Dota 2 East": "208.78.164.1"
}

inputTime = input("Input Time in seconds.")

# input time in (even int)seconds to run and targets
loopPing(inputTime,targets)