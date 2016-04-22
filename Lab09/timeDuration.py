

class TimeSpan:

    def __init__(self, weeks, days, hours):
        if (type(weeks) != int or type(days) != int or type(hours) != int):
            raise TypeError("only ints are accepted")
        if (weeks < 0 or days < 0 or hours < 0 ):
            raise ValueError("values have to be positive")
        self.hours = hours % 24
        self.days = (days + (hours // 24)) % 7
        self.weeks = weeks +  ((days + (hours // 24)) // 7)

    def __str__(self):
        if self.weeks < 10:
            sweek = "0" + str(self.weeks)
        else:
            sweek = str(self.weeks)
        if self.hours < 10:
            shours = "0" + str(self.hours)
        else:
            shours = str(self.hours)
        return sweek + "W " + str(self.days) + "D " + shours + "H"

    def getTotalHours(self):
        total = (self.weeks * (7* 24) ) + (self.days *24) + self.hours
        return total


    def __add__(self, other):
        if isinstance(self, TimeSpan) and isinstance(other, TimeSpan):
            weeks = self.weeks + other.weeks
            hours = self.hours + other.hours
            days = self.days + other.days
            return TimeSpan(weeks,days,hours)
        else:
            raise TypeError ("TimeSpan expected")

    __radd__ = __add__

    def __mul__(self, other):
        if isinstance(self, TimeSpan) and isinstance(other, int):
            if (other <= 0):
                raise ValueError("has to be grater than zero")
            weeks = self.weeks * other
            hours = self.hours * other
            days = self.days * other
            return TimeSpan(weeks,days,hours)
        else:
            raise TypeError ("int expected")

    __rmul__ = __mul__


if __name__ == '__main__':
    d = TimeSpan(3, 14, 188)
    expectedValue = 6, 0, 20
    actualValue = d.weeks, d.days, d.hours
    print (actualValue)
