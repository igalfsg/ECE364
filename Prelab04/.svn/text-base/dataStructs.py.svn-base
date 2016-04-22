import glob
import pprint
from collections import Counter
import string


def getWordFrequency():
    filelist = glob.glob('files/*')
    words = []
    for nombre in filelist:
        with open(nombre, 'r') as myFile:
            all_lines= myFile.readlines()
        for line in all_lines:
            exclude = set(string.punctuation)
            s = ''.join(ch for ch in line if ch not in exclude)
            words.append(s)
    palabras = tuple(words)
    d = dict()
    for lwords in palabras:
        word = lwords.split()
        for i in word:
            if (d.get(i, "notfound") == "notfound"):
                d[i] = 1
            else:
                d[i] +=1
    return d


def getDuplicates():
    filelist = glob.glob('files/*')
    filecont = []
    filenom = []
    groupn = []
    d = dict()
    for nombre in filelist:
        with open(nombre, 'r') as myFile:
            all_lines= myFile.readlines()
            filecont.append(all_lines)
            filenom.append(nombre[6:-4])
    for i in filecont:
        for k in filecont:
            if i == k:
                ind = filecont.index(k)
                groupn.append(filenom[ind])
                filecont.remove(k)
                filenom.remove(filenom[ind])
        if (len(groupn) > 1):
            #get word count and add to dictionary
            exclude = set(string.punctuation)
            s = ''.join(ch for ch in i[0] if ch not in exclude)
            wcount = len(set(s.split()))
            snams = sorted(groupn)
            d[snams[0]] = (wcount, snams)

        groupn = []
    return d


def getPurchaseReport():
    prices = dict()
    costs = dict()
    with open ('purchases/Item List.txt','r') as myFile:
        all_lines= myFile.readlines()
        all_lines.remove(all_lines[0])
        all_lines.remove(all_lines[0])
    for line in all_lines:
        newl = line.split()
        price = float(newl[1][1:])
        prices [newl[0]] = price
    #pprint.pprint(prices)
    filelist = glob.glob('purchases/purchase*')
    for nombre in filelist:
        suma = 0
        with open(nombre, 'r') as myFile:
            all_lines= myFile.readlines()
            all_lines.remove(all_lines[0])
            all_lines.remove(all_lines[0])
        for line in all_lines:
            newl = line.split()
            quantity = float(newl[1])
            producto = newl[0]
            suma += round((prices.get(producto) *   quantity), 2)
        costs[int(nombre[19:-4])] = round(suma, 2)
    return costs


def getTotalSold():
    prices = dict()
    with open ('purchases/Item List.txt','r') as myFile:
        all_lines= myFile.readlines()
        all_lines.remove(all_lines[0])
        all_lines.remove(all_lines[0])
    for line in all_lines:
        newl = line.split()
        prices [newl[0]] = 0
    filelist = glob.glob('purchases/purchase*')
    for nombre in filelist:
        with open(nombre, 'r') as myFile:
            all_lines= myFile.readlines()
            all_lines.remove(all_lines[0])
            all_lines.remove(all_lines[0])
        for line in all_lines:
            newl = line.split()
            prices [newl[0]] +=int(newl[1])
    return prices
if __name__ == '__main__':
    getTotalSold()