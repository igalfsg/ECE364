import glob
import pprint
from collections import Counter
import string

def rowSumIsValid(mat):
    first_sum=0
    suma = 0
    for row in mat:
        suma = 0
        for thing in row:
            suma += thing
        if first_sum == 0:
            first_sum = suma
        elif first_sum != suma:
          return False
    return True

def columnSumIsValid(mat):
    first_sum=0
    suma = 0
    for k in range(len(mat)):
        suma = 0
        for row in mat:
            for i in range(len(row)):
                suma += mat[i][k]
        if first_sum == 0:
            first_sum = suma
        elif first_sum != suma:
          return False
    return True

def magicSquareIsValid(filePath):
    mat = []
    with open (filePath,'r') as myFile:
        all_lines= myFile.readlines()
    for line in all_lines:
        newl = line.split()
        for elemen in range(len(newl)):
            newl[elemen] = int(newl[elemen])
        mat.append(newl)
    col = columnSumIsValid(mat)
    row = rowSumIsValid(mat)
    print (col)
    if col == False:
        return  False
    if row == False:
        return row
    return True

def getTotalCost(itemSet):
    ultimo = dict()
    filelist = glob.glob('Stores/*')
    for nombre in filelist:
        cosas = dict()
        class_num = nombre[7:-4]
        with open(nombre, 'r') as myFile:
            all_lines= myFile.readlines()
            all_lines.remove(all_lines[0])
            all_lines.remove(all_lines[0])
            all_lines.remove(all_lines[0])
            #pprint.pprint(all_lines)
        for line in all_lines:
            newl = line.split()
            precio = newl[3]
            nomb = newl[0]+" "+ newl[1]
            #print(nomb)
            cosas [nomb] = float(precio[1:])
            #print (type( cosas))
        for madre in itemSet:
            temporal = cosas.get(madre[0], "nohay")
            if temporal != "nohay":
                if (ultimo.get(class_num,"nohay")) == "nohay":
                    ultimo[class_num] = 0
                #print (temporal, madre[1])
                ultimo [class_num] = round (ultimo [class_num]+ round (temporal * madre[1],2),2)

    return ultimo

def getBestPrices(cpuSet):
    ultimo = dict()
    neta  =  dict()
    filelist = glob.glob('Stores/*')
    for nombre in filelist:
        class_num = nombre[7:-4]
        with open(nombre, 'r') as myFile:
            all_lines= myFile.readlines()
            all_lines.remove(all_lines[0])
            all_lines.remove(all_lines[0])
            all_lines.remove(all_lines[0])
        for line in all_lines:
            newl = line.split()
            precio = newl[3]
            finpre = float (precio[1:])
            nomb = newl[0]+" "+ newl[1]
            #print(nomb)
            if (ultimo.get(nomb,"nohay")) == "nohay":
                ultimo [nomb] = (round(finpre,2), class_num)
            else:
                valor =  ultimo.get(nomb,"nohay")
                curval = valor[0]
                if curval > round(finpre,2):
                    ultimo [nomb] = (round(finpre,2), class_num)
    for madre in cpuSet:
        neta[madre] = ultimo[madre]
    return neta


def getMissingItems():
    filelist = glob.glob('Stores/*')
    allstuff = []
    allstores = []
    stores = dict()
    for nombre in filelist:
        class_num = nombre[7:-4]
        allstores.append(class_num)
        with open(nombre, 'r') as myFile:
            all_lines= myFile.readlines()
            all_lines.remove(all_lines[0])
            all_lines.remove(all_lines[0])
            all_lines.remove(all_lines[0])
        for line in all_lines:
            newl = line.split()
            nomb = newl[0]+" "+ newl[1]
            allstuff.append(nomb)

            if (stores.get(nomb,"nohay")) == "nohay":
                stores [class_num] = s =[]
            stores[class_num] =s.append(nomb)

    setstuff = set (allstuff)
    for tienda in allstores:
        for cpu in allstuff:
            return None






if __name__ == '__main__':
    cpuSet = {'Intel i7-5950HQ', 'Intel i7-4700HQ', 'Intel i7-4702EC', 'Intel i7-4702MQ', 'Intel i7-6770HQ'}
    expectedValue = {'Intel i7-4700HQ': (801.98, 'TigerDirect'),
                             'Intel i7-4702EC': (1202.88, 'NewEgg'),
                             'Intel i7-4702MQ': (779.67, 'NewEgg'),
                             'Intel i7-5950HQ': (626.66, 'Jet'),
                             'Intel i7-6770HQ': (1293.09, 'NewEgg')}
    actualValue = getBestPrices(cpuSet)
    pprint.pprint(actualValue)