# Here are the Definitions of methods
import os
from datetime import datetime
import time

def loopPing(inputTime,targets):
    for y in range(0,int(inputTime/2)):
        for curTarget in targets:
            testPing(targets[curTarget],curTarget)
        time.sleep(1)


def testPing(targetIP,targetName): 
    response = os.system("ping -n 1 " + targetIP)
    failure = "Can't Reach: " + targetName + " Time: " + str(datetime.now().time()) + "\n"
    if response != 0:
        with open("logs.txt", "a") as myfile:
            myfile.write(failure)
