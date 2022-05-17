# Here are the Definitions of methods
import os
from datetime import datetime


def loopTime(inputTime): 
    test = inputTime


def testPing(targetIP,targetName): 
    response = os.system("ping -c 1 " + targetIP)

    if response != 0:
        with open("logs.txt", "a") as myfile:
            myfile.write("Can't Reach: ",targetName, " Time: ",datetime.now().time())
