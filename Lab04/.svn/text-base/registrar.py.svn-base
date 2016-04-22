import glob
import pprint
from collections import Counter
import string

def getDetails():
    students = dict()
    retdict = dict()
    classgrades = dict()
    with open ('files/students.txt','r') as myFile:
        all_lines= myFile.readlines()
        all_lines.remove(all_lines[0])
        all_lines.remove(all_lines[0])
    for line in all_lines:
        newl = line.split()
        students [newl[0]+" " + newl[1] + " " +newl[2]] = newl[4]
        retdict [newl[0]+" " + newl[1] + " " +newl[2]] = set()
    #done with student reading
    filelist = glob.glob('files/EECS*')
    for nombre in filelist:
        class_num = nombre[10:-4]
        with open(nombre, 'r') as myFile:
            all_lines= myFile.readlines()
            all_lines.remove(all_lines[0])
            all_lines.remove(all_lines[0])
        for line in all_lines:
            newl = line.split()
            classgrades [newl[0]] = int(newl[1])
        for key, value in students.items():
            tempt =  (class_num, classgrades.get(value, "nothere"))
            if tempt[1] != "nothere":
                retdict[key].add(tempt)
        classgrades = dict()
    return retdict

def getStudentList (classNumber):
    students = dict()
    lr = []
    with open ('files/students.txt','r') as myFile:
        all_lines= myFile.readlines()
        all_lines.remove(all_lines[0])
        all_lines.remove(all_lines[0])
    for line in all_lines:
        newl = line.split()
        students [newl[4]] = newl[0]+" " + newl[1] + " " +newl[2]
    filelist = glob.glob('files/EECS*')
    for nombre in filelist:
        class_num = nombre[10:-4]
        if class_num == classNumber:
            with open(nombre, 'r') as myFile:
                all_lines= myFile.readlines()
                all_lines.remove(all_lines[0])
                all_lines.remove(all_lines[0])
            for line in all_lines:
                newl = line.split()
                nomb = students[newl[0]]
                lr.append(nomb)
    return sorted(lr)

def searchForName(sname):
    det = getDetails()
    r = dict()
    sset = det.get(sname, "nothere")
    if sset == "nothere":
        return r
    for element in sset:
        r [element[0]] = element[1]
    return r


def searchForID(sid):
    students = dict()
    lr = []
    with open ('files/students.txt','r') as myFile:
        all_lines= myFile.readlines()
        all_lines.remove(all_lines[0])
        all_lines.remove(all_lines[0])
    for line in all_lines:
        newl = line.split()
        students [newl[4]] = newl[0]+" " + newl[1] + " " +newl[2]
    return searchForName(students.get(sid, "nothere"))


def findScore (stname, class_num):
    resu = searchForName(stname)
    cali = resu.get(class_num,"nothere")
    if cali == "nothere":
        return None
    return cali

def getHighest(cl_num):
    max = 0
    students = dict()
    with open ('files/students.txt','r') as myFile:
        all_lines= myFile.readlines()
        all_lines.remove(all_lines[0])
        all_lines.remove(all_lines[0])
    for line in all_lines:
        newl = line.split()
        students [newl[4]] = newl[0]+" " + newl[1] + " " +newl[2]
    filelist = glob.glob('files/EECS*')
    for nombre in filelist:
        class_num = nombre[10:-4]
        if class_num == cl_num:
            with open(nombre, 'r') as myFile:
                all_lines= myFile.readlines()
                all_lines.remove(all_lines[0])
                all_lines.remove(all_lines[0])
            for line in all_lines:
                newl = line.split()
                if int(newl[1]) > max:
                    max = int(newl[1])
                    snum = students.get(newl[0], "nothere")
            x = (snum, max)
            return x
    return ()

def getLowest(cl_num):
    max = 500
    students = dict()
    with open ('files/students.txt','r') as myFile:
        all_lines= myFile.readlines()
        all_lines.remove(all_lines[0])
        all_lines.remove(all_lines[0])
    for line in all_lines:
        newl = line.split()
        students [newl[4]] = newl[0]+" " + newl[1] + " " +newl[2]
    filelist = glob.glob('files/EECS*')
    for nombre in filelist:
        class_num = nombre[10:-4]
        if class_num == cl_num:
            with open(nombre, 'r') as myFile:
                all_lines= myFile.readlines()
                all_lines.remove(all_lines[0])
                all_lines.remove(all_lines[0])
            for line in all_lines:
                newl = line.split()
                if int(newl[1]) < max:
                    max = int(newl[1])
                    snum = students.get(newl[0], "nothere")
            x = (snum, max)
            return x
    return ()

def getAverageScore(sname):
    count = 0
    suma = 0
    di = searchForName(sname)
    for i in di.values():
        suma +=  i
        count += 1
    if count == 0:
        return None
    return (suma/count)

if __name__ == '__main__':
    print(getAverageScore("James F Hughes"))