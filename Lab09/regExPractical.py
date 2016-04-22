import os.path
import re
import sys
import pprint
# * 0 or more + 1 or more ? one ot zero ^start of string $end of string

def getAddress(sentence):
    address = re.search("([a-fA-F0-9]{2}[:-]{1}[a-fA-F0-9]{2}[:-]{1}[a-fA-F0-9]{2}[:-]{1}[a-fA-F0-9]{2}[:-]{1}[a-fA-F0-9]{2}[:-]{1}[a-fA-F0-9]{2})", sentence)
    if address:
        return address.group(1)
    else:
        return None

def getSwitches (commandline):
    lis = []
    swit = re.findall("[+]{1}([a-z]+)\s+([\w]+)", commandline)
    for i in swit:
        t = (i.group(1), i.group(2))
        lis.append(t)
    return lis
def getElements(fullAddress):
    address = re.match("http{1}[s]?://{1}([A-Za-z0-9.]+)[/]{1}([A-Za-z0-9]+)[/]{1}([A-Za-z0-9]+)$", fullAddress)
    if address:
        return (address.group(1), address.group(2), address.group(3))
    else:
        return None

if __name__ == '__main__':
    commandline = r"myScript.bash +v  \i 2   +p  /local/bin/somefolder"
    expectedValue = [("i", "2"), ("p", "/local/bin/somefolder")]
    actualValue = getSwitches(commandline)
    print(actualValue)