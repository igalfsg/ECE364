import HardwareTasks

def verilog2vhdl(ver_line):
    try:
        igs = HardwareTasks.processLine(ver_line)
    except ValueError:
        return "Error: Bad Line."
    strin = igs[1] + ": " + igs[0] + " "
    vals ="("
    for i in igs[2]:
        vals += i[0] + "=>" + i[1]
        vals += ", "
    vals = vals[:-2]
    vals +=");"
    return strin +  "PORT MAP" + vals

def convertNetlist(sourceFlie, targetFile):
    with open(sourceFlie, 'r') as myFile:
        all_lines = myFile.readlines()
    temp = ""
    for line in all_lines:
        temp += verilog2vhdl(line) + "\n"
    temp = temp[:-1]
    with open(targetFile, 'w') as myFile:
        myFile.write(temp)


if __name__ == "__main__":
    convertNetlist("verilog_test.v", "actualFileName.txt")