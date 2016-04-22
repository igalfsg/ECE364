import math
class PointND:
    def __init__(self, *args):
        self.t = args
        self.n = len(self.t)
        for i in self.t:
            if type(i) != float:
                raise ValueError("Cannot instantiate an object with non-float valuses.")


    def __str__(self):
        solution = tuple(['{:.2f}'.format(round(x,2)) if isinstance(x, float) else x for x in self.t])
        s = "("
        for i in solution:
            s += i
            s += ", "
        s = s [:-2]
        s += ")"
        return str(s)
    def __hash__(self):
        return hash(self.t)

    def distanceFrom(self, other):
        if (self.n != other.n):
            raise ValueError("Cannot calculate distance between points of different cardinality.")
        else:
            euc = 0
            for i in range(self.n):
                euc += pow((self.t[i] - other.t[i]), 2)
        return math.sqrt(euc)

    def nearestPoint(self, points):
        if (0 == len(points)):
            raise ValueError("Input cannot be empty.")
        else:
            max = self.distanceFrom(points[0])
            for i in points:
                temp = self.distanceFrom(i)
                if temp < max:
                    max = temp
                    j = i
            return j

    def clone(self):
        return PointND(*self.t)

    def __add__(self, other):
        if isinstance(self, PointND) and isinstance(other, PointND):
            if (self.n != other.n):
                raise ValueError("Cannot calculate distance between points of different cardinality.")
            else:
                li = []
                for i in range(self.n):
                    euc= self.t[i] + other.t[i]
                    li.append(euc)
                    n = tuple(li)
                return PointND(*n)
        elif isinstance(self, PointND) and isinstance(other, float):
            li = []
            for i in self.t:
                euc = i + other
                li.append(euc)
                n = tuple(li)
            return PointND(*n)

    __radd__ =  __add__


    def __sub__(self, other):
        if isinstance(self, PointND) and isinstance(other, PointND):
            if (self.n != other.n):
                raise ValueError("Cannot calculate distance between points of different cardinality.")
            else:
                li = []
                for i in range(self.n):
                    euc= self.t[i] - other.t[i]
                    li.append(euc)
                    n = tuple(li)
                return PointND(*n)
        elif isinstance(self, PointND) and isinstance(other, float):
            li = []
            for i in range(self.n):
                euc = self.t[i] - other
                li.append(euc)
                n = tuple(li)
            return PointND(*n)

    def __mul__(self, other):
        if isinstance(self, PointND) and isinstance(other, float):
            li = []
            for i in range(self.n):
                euc = self.t[i] * other
                li.append(euc)
                n = tuple(li)
            return PointND(*n)
    __rmul__ = __mul__

    def __truediv__(self, other):
        if isinstance(self, PointND) and isinstance(other, float):
            li = []
            for i in range(self.n):
                euc = self.t[i] / other
                li.append(euc)
                n = tuple(li)
            return PointND(*n)



    def __neg__(self):
        li = []
        for i in self.t:
            euc = i * -1
            li.append(euc)
            n = tuple(li)
        return PointND(*n)

    def __getitem__(self, k):
        return self.t[k]

    def __eq__(self, other):
        if(self.n != other.n):
            raise ValueError("Cannot compare points with different cardinalities.")
        for i in range(self.n):
            if(self.t[i] != other.t[i]):
                return False
        return True

    def __lt__(self, other): #Overloads the < operator
        if(self.n != other.n):
            raise ValueError("Cannot compare points with different cardinalities.")
        li = []
        for i in range(self.n):
            li.append(0.0)
        n = tuple(li)
        org = PointND(*n)
        if(self.distanceFrom(org) >= other.distanceFrom(org)):
            return False
        return True

    def __le__(self, other):
        if(self.n != other.n):
            raise ValueError("Cannot compare points with different cardinalities.")
        li = []
        for i in range(self.n):
            li.append(0.0)
        n = tuple(li)
        org = PointND(*n)
        if(self.distanceFrom(org) > other.distanceFrom(org)):
            return False
        return True



    def __gt__(self, other): #Overloads the > operator
        if(self.n != other.n):
            raise ValueError("Cannot compare points with different cardinalities.")
        li = []
        for i in range(self.n):
            li.append(0.0)
        n = tuple(li)
        org = PointND(*n)
        if(self.distanceFrom(org) <= other.distanceFrom(org)):
            return False
        return True

    def __ge__(self, other): #Overloads the >= operator
        if(self.n != other.n):
            raise ValueError("Cannot compare points with different cardinalities.")
        li = []
        for i in range(self.n):
            li.append(0.0)
        n = tuple(li)
        org = PointND(*n)
        if(self.distanceFrom(org) < other.distanceFrom(org)):
            return False
        return True


class Point3D(PointND):
    def __init__(self, x=0.0, y=0.0, z=0.0):

        self.x = x
        self.y = y
        self.z = z
        PointND.__init__(self, x, y, z)


class PointSet:
    def __init__(self, **kwargs):
        if (len(kwargs) == 0):
            self.points = set()
            self.n = 0
        elif("pointList" in kwargs):
            if len(kwargs["pointList"]) == 0:
                raise ValueError("'pointList' input parameter cannot be empty.")
            self.n = kwargs["pointList"][0].n
            self.points = set()
            for point in kwargs["pointList"]:
                if self.n != point.n:
                    raise ValueError("Expecting a point with cardinality {0}.".format(self.n))
                self.points.add(point)
        else:
            raise KeyError("'pointList' input parameter not found.")


    def addPoint(self, p):
        if self.n != p.n:
            raise ValueError("Expecting a point with cardinality {0}.".format(self.n))
        self.points.add(p)


    def count(self):
        return len(self.points)

    def computeBoundingHyperCube(self):
        minp = [999999999999999999999999999999] *self.n
        maxp = [0] * self.n
        for point in self.points:
            for i in range(self.n):
                if point[i] > maxp[i]:
                    maxp[i] = point[i]
                if point[i] < minp[i]:
                    minp[i] = point[i]
        minpoin = PointND(*minp)
        maxpoin = PointND(*maxp)
        return (minpoin, maxpoin)

    def computeNearestNeighbors(self, otherPoints):
        lis = []
        for point in self.points:
            min = 9999999999999999999999999999999999999999999999999999999999999999999
            for otherp in otherPoints.points:
                if point.distanceFrom(otherp) < min:
                    minp = otherp
                    min = point.distanceFrom(otherp)
            t = (point, minp)
            lis.append(t)
        return lis


    def __add__(self, other):

        if isinstance(other, PointND):
            if self.n != other.n:
                raise ValueError("Expecting a point with cardinality {0}.".format(self.n))
            self.points.add(other)
        return self
    __radd__ = __add__

    def __sub__(self,other):
        if other in self.points:
            self.points.remove(other)
        return self

    def __contains__(self, other):
        if self.n != other.n:
            raise ValueError("Expecting a point with cardinality {0}.".format(self.n))
        if other in self.points:
            return True
if __name__ == '__main__':
    expectedValue = 3.0