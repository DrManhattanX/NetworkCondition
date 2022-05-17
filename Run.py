# This is where to call the methods defined in Definitions.py
from Definitions import *

# Target name and IP/address
targets = {
    "Zay": "192.168.0.104",
    "Google": "www.Google.com"
}

# input time in (even int)seconds to run and targets
loopPing(10,targets)