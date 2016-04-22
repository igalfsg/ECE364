
import sys

def parse_file (file_name):
    try:
        with open(file_name, 'r') as myFile:
            all_lines = myFile.readlines()
            for line in all_lines:
                suma = 0
                letras = ""
                cuenta = 0
                vallist = line.split()
                for i in vallist:
                    try:
                        suma +=float(i)

                    except (ValueError):
                        letras += i + " "
                    else:
                        cuenta += 1
                if suma != 0:
                    avgr =  suma/cuenta
                    if letras != "":
                        print("{0:.3f}".format(avgr) + " " + letras[:-1])
                    else:
                        print("{0:.3f}".format(avgr))
                elif letras != "":
                    print(letras[:-1])

    except(IOError):
        print (file_name, " is not a readable file.")




if __name__ == "__main__":
    if (len(sys.argv) == 2):
        parse_file(sys.argv[1])
    else:
        print("Usage: parse.py [filename]")