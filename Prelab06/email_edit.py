import re
def email():
    with open('Part2.in', 'r') as myFile:
        all_lines = myFile.readlines()
        for line in all_lines:
            isa = re.match("[\w.-]+(@){1}(purdue.edu){1}", line)
            if(isa):
                temp = re.sub('@purdue.edu', '@ecn.purdue.edu', line)
                temp = re.sub('\n', '', temp)
                print( temp + '/100')
            else:
                isa = re.match("[\w.-]+(@ecn.purdue.edu){1}", line)
                if (isa):
                    temp = re.sub('\n', '', line)
                    print( temp + '/100')

if __name__ == '__main__':
    email()