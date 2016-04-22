import re
import string


def idIsAcceptable(ver_id):
    igs = re.match('[\w_]+$', ver_id)
    if igs:
        return True
    return False
def processSingle(ver_assignment):
    igs =re.search('^[.]{1}([\w_]+)[(]([\w_]+)[)]{1}$', ver_assignment)
    if igs:
        return (igs.group(1), igs.group(2))
    raise ValueError(ver_assignment)

def processLine(ver_line):
    lis = ver_line.split()
    lis2 = []
    if len(lis) == 3:
        lis3 = lis[2].split(",")
        lis3[0] = lis3[0][1:]
        lis3[-1] = lis3[-1][:-1]
        for i in lis3:
            lis2.append(processSingle(i))
    else:
        if lis[-1] != ")":
            raise ValueError(ver_line)
        for i in range(3, (len(lis) - 1)):
            if(lis[i][-1] == ","):
                lis2.append(processSingle(lis[i][:-1]))
            elif (i == (len(lis) - 2)):
                lis2.append(processSingle(lis[i]))
            else:
                raise ValueError(ver_line)

    if idIsAcceptable(lis[0]) == False or idIsAcceptable(lis[1]) == False:
        raise ValueError(ver_line)
    t = tuple(lis2)
    return (lis[0], lis[1], t)



if __name__ == "__main__":
    line = "  OAI21X1 U16 ( .A(shift_strobe), .B(n4), .C(n10), .Y(n30) ))"

    assignmentList = ("A", "n32"), ("B", "n5"), ("C", "n3"), ("D", "n6"), ("Y", "n25")
    expectedValue =  "OAI22X1", "U11", assignmentList
    actualValue = processLine(line)
    print (actualValue)
