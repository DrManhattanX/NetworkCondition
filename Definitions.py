# Here are the Definitions of methods
import os

def loopTime(inputTime): 
    test = inputTime


def testPing(targetIP,targetName): 
    response = os.system("ping -c 1 " + targetIP)

    if response != 0:
        print ("Can't Reach: ",targetName)
