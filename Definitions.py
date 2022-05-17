# Here are the Definitions of methods
import os
from datetime import datetime
import time
import subprocess
process = subprocess.Popen(['ping','-c' ,'1', '8.8.8.8'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = process.communicate()
returncode = process.returncode
print(returncode)



def loopPing(inputTime,targets):
    for y in range(0,int(inputTime/2)):
        print("loops left" + y)
        for curTarget in targets:
            testPing(targets[curTarget],curTarget)
        time.sleep(1)


def testPing(targetIP,targetName): 
    process = subprocess.Popen(['ping','-n' ,'1', targetIP], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    returncode = process.returncode
    failure = "Can't Reach: " + targetName + " Time: " + str(datetime.now().time()) + "\n"
    if returncode != 0:
        with open("logs.txt", "a") as myfile:
            myfile.write(failure)
