def getPairwiseDifference(vec):
    if type(vec) != list:
        return None
    if len(vec) == 0:
        return None
    f_list = []
    for i in range (1, len(vec)):
        resta = vec[i] - vec[i-1]
        f_list.append(resta)
    return f_list

def flatten (l):
    f_list = []
    if type(l) != list:
        return None
    for i in l:
        if type(i) == list:
            for k in i:
                f_list.append(k)
        else:
            return None
    return f_list


def partition(l,n):
    sub = []
    count = 1
    fl = []
    if type(l) != list:
        return None
    if len(l) == 0:
        return None
    for i in l:
        sub.append(i)
        if count == n:
            fl.append(sub)
            sub = []
            count = 1
        else:
            count +=1
    if count > 1:
        fl.append(sub)
    return fl


def rectifySignal(signal):
    if type(signal) != list:
        return None
    if len(signal) == 0:
        return None
    fl = []
    for i in signal:
        if i < 0:
            fl.append(0)
        else:
            fl.append(i)
    return fl


def floatRange(a, b, s):
    steps = 1 / s
    fl = []
    if b<=a:
        return None
    fl.append(a)
    for i in range (a,b):
        val = i
        k = 0
        while k <steps:
            val = val + s
            val = round(val, 1)
            fl.append(val)
            k +=1
    return fl

def getLongestWord(sentence):
    if type(sentence) != str:
        return None
    words = sentence.split()
    if len(words) <= 1:
        return None
    max = 0
    for word in words:
        tama = len(word)
        if tama > max:
            max = tama
            max_s = word
    return max_s

def decodeNumbers(l):
    if type(l) != list:
        return None
    palabr = []
    for i in l:
        if type(i) != int:
            return None
        letra = chr(i)
        palabr.append(letra)
    return "".join(palabr)

def getCreditCard(s):
    if type(s) != str:
        return None
    if len(s) == 0:
        return None
    fl = []
    for i in range (0,len(s)):
        if s[i].isdigit():
            fl.append(int(s[i]))

    return fl



if __name__ == '__main__':
    s = "Sherlock Holmes 1234-6598-7845-2050"
    expectedValue = [1, 2, 3, 4, 6, 5, 9, 8, 7, 8, 4, 5, 2, 0, 5, 0]
    actualValue = getCreditCard(s)
    print (actualValue)