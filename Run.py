# This is where to call the methods defined in Definitions.py
from Definitions import *

# Target name and IP/address
targets = {
    "Zay": "192.168.0.104",
    "Google": "www.Google.com",
    "Brian": "74.135.15.103"
}

# input time in (even int)seconds to run and targets
loopPing(60,targets)