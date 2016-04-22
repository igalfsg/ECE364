import re
import sys
def ip_detect(input_file):
     with open(input_file, 'r') as myFile:
        all_lines = myFile.readlines()
        for line in all_lines:
            formatchk = re.match(
                "(^[2][0-5][0-5]|^[0-1]{0,1}[0-9]{1,2})\.([0-2][0-5][0-5]|[0-1]{0,1}[0-9]{1,2})\.([0-2][0-5][0-5]|[0-1]{0,1}[0-9]{1,2})\.([0-2][0-5][0-5]|[0-1]{0,1}[0-9]{1,2})\:([3][0-2][0-7][0-6][0-7]|[3][0-1][0-9]{1,3}|[0-2]?[0-9]{1,4})$", line)
            if (formatchk):#the formatr is correct
                rootchk = re.match(
                "(^[2][0-5][0-5]|^[0-1]{0,1}[0-9]{1,2})\.([0-2][0-5][0-5]|[0-1]{0,1}[0-9]{1,2})\.([0-2][0-5][0-5]|[0-1]{0,1}[0-9]{1,2})\.([0-2][0-5][0-5]|[0-1]{0,1}[0-9]{1,2})\:([1][0][0-2][0-4]|[0]?[0-9]{1,3})$", line)
                if(rootchk):
                    print(line[:-1] + " " + "Valid (root privileges required)")
                else:
                    print(line[:-1] + " " + "Valid")
            else:
                ipcheck = re.match(
                "(^[2][0-5][0-5]|^[0-1]{0,1}[0-9]{1,2})\.([0-2][0-5][0-5]|[0-1]{0,1}[0-9]{1,2})\.([0-2][0-5][0-5]|[0-1]{0,1}[0-9]{1,2})\.([0-2][0-5][0-5]|[0-1]{0,1}[0-9]{1,2})\:\w*$", line)
                if (ipcheck):
                    print(line[:-1] + " " + "Invalid Port Number")
                else:
                    print(line[:-1] + " " + "Invalid IP Address")
if __name__ == '__main__':
    if len (sys.argv) == 2:
        inputfile = sys.argv[1]
        ip_detect(inputfile)
    else:
        print("invalid num args")