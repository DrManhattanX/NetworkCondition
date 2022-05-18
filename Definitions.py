# Here are the Definitions of methods
import os
from datetime import datetime
import time
import subprocess
clear = lambda: os.system('cls')

def loopPing(inputTime,targets):
    connectionsLost = {
        "Google": 0,
    }
    for curTarget in targets:
        connectionsLost[curTarget] = 0
    for y in range(0,int(inputTime)):
        clear()
        print("loops left " + str(int(inputTime) - y))
        for curTarget in targets:
            testPing(targets[curTarget],curTarget,connectionsLost)
        time.sleep(0.5)
    clear()
    print("Below are connections with failures to ping \n")
    for cur in connectionsLost:
        print(cur + ": " + connectionsLost[cur] + "\n")


def testPing(targetIP,targetName,connectionsLost): 
    process = subprocess.Popen(['ping','-n' ,'1', targetIP], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    returncode = process.returncode
    failure = "Can't Reach: " + targetName + " Time: " + str(datetime.now().time()) + "\n"
    if returncode != 0:
        with open("logs.txt", "a") as myfile:
            myfile.write(failure)
            connectionsLost[targetName] +=  1
