import os.path
import re
import sys
import pprint
# * 0 or more + 1 or more ? one ot zero ^start of string $end of string
def getRejectedUsers():
    with open('SiteRegistration.txt', 'r') as myFile:
        all_lines = myFile.readlines()
        reg = []
        for line in all_lines:
            regect = re.match("(^[\w\s,]+)[;,\s]*$", line)
            if(regect):
                pan = re.match("(\w+\s\w+)", regect.group(1))
                if pan:
                    reg.append(pan.group(1))
                else:
                    igs = re.match("(\w+),\s(\w+)", regect.group(1))
                    #re.sub("[, ]","",igs)
                    temp = igs.group(2) + " " + igs.group(1)
                    reg.append(temp)
        reg.sort()
    return reg

def getUsersWithEmails():
    with open('SiteRegistration.txt', 'r') as myFile:
        all_lines = myFile.readlines()
        ret = dict()
        for line in all_lines:
            email = re.search("([\w.-]+@[\w.-]+)", line)
            name = re.search("(^[\w\s,]+)", line)
            #format name
            if(email):
                pan = re.match("(\w+\s\w+)", name.group(1))
                if pan:
                    temp = pan.group(1)
                else:
                    igs = re.match("(\w+),\s(\w+)", name.group(1))
                    temp = igs.group(2) + " " + igs.group(1)
                ret [temp] = email.group(1)
    return ret
def getUsersWithPhones():
    with open('SiteRegistration.txt', 'r') as myFile:
        all_lines = myFile.readlines()
        ret = dict()
        for line in all_lines:
            phone = re.search("[(]?([0-9]{3})[)]?\s?[-]?([0-9]{3})?\s?[-]?([0-9]{4})", line)
            name = re.search("(^[\w\s,]+)", line)
            #format name
            if(phone):
                pan = re.match("(\w+\s\w+)", name.group(1))
                if pan:
                    temp = pan.group(1)
                else:
                    igs = re.search("([A-Za-z]+?),{1}\s{1}([A-Za-z]+)", name.group(1))
                    temp = igs.group(2) + " " + igs.group(1)
                numbers = "(" + phone.group(1) +") " + phone.group(2) +"-"+ phone.group(3)
                ret [temp] = numbers
    return ret

def getUsersWithStates():
    with open('SiteRegistration.txt', 'r') as myFile:
        all_lines = myFile.readlines()
        ret = dict()
        for line in all_lines:
            state = re.search("(\w+$|\w+\s\w+$)", line)
            name = re.search("(^[\w\s,]+)", line)
            if(state):
                pan = re.match("(\w+\s\w+)", name.group(1))
                if pan:
                    temp = pan.group(1)
                else:
                    igs = re.search("([A-Za-z]+?),{1}\s{1}([A-Za-z]+)", name.group(1))
                    temp = igs.group(2) + " " + igs.group(1)
                ret [temp] = state.group(1)
    return ret

def getUsersWithoutEmails():
    emails = getUsersWithEmails()
    phone = getUsersWithPhones()
    state = getUsersWithStates()
    with open('SiteRegistration.txt', 'r') as myFile:
        all_lines = myFile.readlines()
        ret = []
        for line in all_lines:

            name = re.search("(^[\w\s,]+)", line)
            if(name):
                pan = re.match("(\w+\s\w+)", name.group(1))
                if pan:
                    temp = pan.group(1)
                else:
                    igs = re.search("([A-Za-z]+?),{1}\s{1}([A-Za-z]+)", name.group(1))
                    temp = igs.group(2) + " " + igs.group(1)
                chk = emails.get(temp)
                if (chk == None):
                    ck1 = phone.get(temp)
                    ck2 = state.get(temp)
                    if ((ck1 != None) | (ck2 != None)):
                        ret.append(temp)
    ret.sort()
    return ret




def getUsersWithoutPhones():
    emails = getUsersWithEmails()
    phone = getUsersWithPhones()
    state = getUsersWithStates()
    with open('SiteRegistration.txt', 'r') as myFile:
        all_lines = myFile.readlines()
        ret = []
        for line in all_lines:

            name = re.search("(^[\w\s,]+)", line)
            if(name):
                pan = re.match("(\w+\s\w+)", name.group(1))
                if pan:
                    temp = pan.group(1)
                else:
                    igs = re.search("([A-Za-z]+?),{1}\s{1}([A-Za-z]+)", name.group(1))
                    temp = igs.group(2) + " " + igs.group(1)
                chk = phone.get(temp)
                if (chk == None):
                    ck1 = emails.get(temp)
                    ck2 = state.get(temp)
                    if ((ck1 != None) | (ck2 != None)):
                        ret.append(temp)
    ret.sort()
    return ret

def getUsersWithoutStates():
    emails = getUsersWithEmails()
    phone = getUsersWithPhones()
    state = getUsersWithStates()
    with open('SiteRegistration.txt', 'r') as myFile:
        all_lines = myFile.readlines()
        ret = []
        for line in all_lines:

            name = re.search("(^[\w\s,]+)", line)
            if(name):
                pan = re.match("(\w+\s\w+)", name.group(1))
                if pan:
                    temp = pan.group(1)
                else:
                    igs = re.search("([A-Za-z]+?),{1}\s{1}([A-Za-z]+)", name.group(1))
                    temp = igs.group(2) + " " + igs.group(1)
                chk = state.get(temp)
                if (chk == None):
                    ck1 = emails.get(temp)
                    ck2 = phone.get(temp)
                    if ((ck1 != None) | (ck2 != None)):
                        ret.append(temp)
    ret.sort()
    return ret
def getUsersWithCompleteInfo():
    emails = getUsersWithEmails()
    phone = getUsersWithPhones()
    state = getUsersWithStates()
    with open('SiteRegistration.txt', 'r') as myFile:
        all_lines = myFile.readlines()
        ret = dict()
        for line in all_lines:

            name = re.search("(^[\w\s,]+)", line)
            if(name):
                pan = re.match("(\w+\s\w+)", name.group(1))
                if pan:
                    temp = pan.group(1)
                else:
                    igs = re.search("([A-Za-z]+?),{1}\s{1}([A-Za-z]+)", name.group(1))
                    temp = igs.group(2) + " " + igs.group(1)
                chk = state.get(temp)
                ck1 = emails.get(temp)
                ck2 = phone.get(temp)
                if ((ck1 != None) & (ck2 != None) & (chk != None)):
                    ret[temp] = (ck1, ck2, chk)
    return ret
if __name__ == '__main__':
    pprint.pprint(getUsersWithCompleteInfo())