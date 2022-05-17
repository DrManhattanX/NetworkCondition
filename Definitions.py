# Here are the Definitions of methods
import os
from datetime import datetime
import time
import subprocess
clear = lambda: os.system('cls')
connectionsLost = 0

def loopPing(inputTime,targets):
    for y in range(0,int(inputTime/2)):
        clear()
        print("loops left " + str(int(inputTime/2) - y))
        for curTarget in targets:
            testPing(targets[curTarget],curTarget)
        time.sleep(1)
    clear()
    print("Finished with " + str(connectionsLost) + " connections Failed")


def testPing(targetIP,targetName): 
    process = subprocess.Popen(['ping','-n' ,'1', targetIP], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    returncode = process.returncode
    failure = "Can't Reach: " + targetName + " Time: " + str(datetime.now().time()) + "\n"
    if returncode != 0:
        with open("logs.txt", "a") as myfile:
            myfile.write(failure)
            connectionsLost = connectionsLost + 1
