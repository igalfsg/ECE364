import re


class Simulation:
    def __init__(self, simNo, simDate, chipName, chipCount, chipCost):
        self.simulationNumber = simNo
        self.simulationDate = simDate
        self.chipName = chipName
        self.chipCost = chipCost
        self.chipCount = chipCount
        self.simulationCost = chipCount * chipCost

    def __str__(self):
        t = self.chipName + ": " + "{0:03d}".format(self.simulationNumber) + ", " + self.simulationDate + ", $" + "{0:06.2f}".format(self.simulationCost)
        return t

class Employee:
    def __init__(self, employeeName, employeeID):
        self.simulationsDict = dict()
        self.employeeName = employeeName
        self.employeeID = employeeID


    def addSimulation(self, sim):
        self.simulationsDict[sim.simulationNumber] = sim

    def getSimulation(self, simNo):
        val = self.simulationsDict.get(simNo, "no esta")
        if val == "no esta":
            return None
        return val

    def __str__(self):
        s = self.employeeID + ", " + self.employeeName + ": " + "{0:02d}".format(len(self.simulationsDict)) + " Simulations"
        return s

    def getWorkload(self):
        s = self.employeeID + ", " + self.employeeName + ": " + "{0:02d}".format(len(self.simulationsDict)) + " Simulations\n"
        lis = []
        for i in self.simulationsDict:
            line =  self.simulationsDict[i].chipName + ": "
            line += "{0:03d}".format(self.simulationsDict[i].simulationNumber) +", "
            line += self.simulationsDict[i].simulationDate + ", "
            line += "$" + "{0:06.2f}".format(self.simulationsDict[i].simulationCost) + "\n"
            lis.append(line)
        lis.sort()
        for i in lis:
            s += i
        s = s[:-1]
        return s


    def addWorkload(self, fileName):
        with open(fileName, 'r') as myFile:
            all_lines = myFile.readlines()
            all_lines.remove(all_lines[0])
            all_lines.remove(all_lines[0])
        for line in all_lines:
            q = line.split()

            s1 = Simulation (int(q[0]), q[1], q[2], int(q[3]), float(q[4][1:]))
            self.addSimulation(s1)

class Facility:
    def __init__(self, facilityName):
        self.employeesDict = dict()
        self.facilityName = facilityName

    def addEmployee(self, employee):
        self.employeesDict[employee.employeeName] = employee

    def getEmployees(self, *args):
        i = args
        lis = []
        for e in i:
            lis.append(self.employeesDict.get(e))
        return lis

    def __str__(self):
        s = self.facilityName + ": " + "{0:02d}".format(len(self.employeesDict)) + " Employees\n"
        lis = []
        for i in self.employeesDict.keys():
            lis.append(str(self.employeesDict.get(i)) +"\n")
        lis.sort()
        for i in lis:
            s += i
        s = s[:-1]
        return s

    def getSimulation(self, simNo):
        for i in self.employeesDict.keys():
            igs = self.employeesDict.get(i).getSimulation(simNo)
            if igs != None:
                return igs
        return None
if __name__ == '__main__':
    f = Facility("Intel")
    e1 = Employee("Alejandro Carrero", "520-11-9977")
    e2 = Employee("Tracey Driscoll", "741-85-9632")

    e1.addWorkload("workload1.txt")
    e2.addWorkload("workload2.txt")
    f.addEmployee(e1)
    f.addEmployee(e2)

    expectedValue = "Intel: 02 Employees\n"
    expectedValue += "520-11-9977, Alejandro Carrero: 04 Simulations\n"
    expectedValue += "741-85-9632, Tracey Driscoll: 04 Simulations"
    actualValue = str(f)
    print(actualValue)