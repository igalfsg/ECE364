import pprint
from timeDuration import *

def doeventdic():
    with open('Events.txt', 'r') as myFile:
        all_lines = myFile.readlines()
        all_lines.remove(all_lines[0])
        all_lines.remove(all_lines[0])
        d = {}
        for line in all_lines:
            weeks = 0
            hrs = 0
            days = 0
            stuff = line.split()
            if (stuff[1][-1] == 'd'):
                days = int (stuff[1][:-1]) * int (stuff[2])
            elif (stuff[1][-1] == 'h'):
                hrs = int (stuff[1][:-1]) * int (stuff[2])
            elif (stuff[1][-1] == 'w'):
                weeks = int (stuff[1][:-1]) * int (stuff[2])
            ev = d.get(stuff[0], "nah dude")
            if(ev == "nah dude"):
                d[stuff[0]] = TimeSpan(weeks, days, hrs)
            else:
                newev = ev + TimeSpan(weeks, days, hrs)
                d[stuff[0]] = newev
        return d

def getTotalEventSpan(eventName):
    d = doeventdic()
    ev = d.get(eventName, "nah dude")
    if ev == "nah dude":
        raise ValueError("name not found")
    return ev
def rankEventsBySpan(*args):
    i = args
    lis = []
    rlis = []
    for nombre in i:
        nhrrs = getTotalEventSpan(nombre).getTotalHours()
        t = (nhrrs, nombre)
        lis.append(t)
    lis.sort()
    lis.reverse()
    for yo in lis:
       rlis.append(yo[1])
    return rlis
if __name__ == '__main__':
    pprint.pprint(doeventdic())