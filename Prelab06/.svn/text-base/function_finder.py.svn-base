import os.path
import re
import sys

def function_finder(input_file):
    try:
        with open(input_file, 'r') as myFile:
            for line in myFile:
                isfun = re.match("def{1}\s+(\w+)\s*[(]{1}([\w\s=,_-]+)[)]{1}\:", line)
                if isfun:
                    print (isfun.group(1))
                    words = isfun.group(2).split(",")
                    i = 1
                    for word in words:
                        c = re.sub(' ', "", word)
                        print("Arg" + str(i)+ ": " + c)
                        i += 1
    except IOError as err:
        print (input_file + " is not reeadable")
        return



if __name__ == '__main__':
    if len (sys.argv) == 2:
        inputfile = sys.argv[1]
        if os.path.isfile(inputfile) :
            function_finder(inputfile)
        else:
            print (inputfile, " Does not exist")
    else:
        print("invalid num args")
        function_finder('module1.py')