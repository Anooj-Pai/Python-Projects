class Date(object):
    def __init__(self,z0=1900,x0=1,y0=1):
        self.x = x0
        self.z = z0
        self.y = y0
    def __str__(self):
        return "{}/ {}/ {}".format(self.z,str(self.x).rjust(2,'0'),str(self.y).rjust(2,'0'))
    def same_day_in_year(self,other):
        if self.y == other.y and self.x == other.x:
            return True
        else:
            return False
    def is_leap_year(self):
        if ((self.z%4 == 0) or (self.z%400 == 0)):
            return True
        else:
            return False
    def __lt__(self,other):
        if self.z < other.z:
            return True
        elif self.z == other.z:
            if self.x < other.x:
                return True
            elif self.y < other.y:
                return True
        return False
    
    def __gt__(self,other):
        if self.z > other.z:
            return True
        elif self.z == other.z:
            if self.x > other.x:
                return True
            elif self.y > other.y:
                return True
        return False
if __name__ == "__main__":
    d1 = Date(1972, 3, 27)
    d2 = Date(1998, 4, 13)
    d3 = Date(1998, 5, 13)
    d4 = Date(1998, 4, 11)
    d5 = Date(1900, 11, 5)
    d6 = Date(2012, 5, 8)
    print("d1: " + str(d1))
    print("d2: " + str(d2))
    print("d3: " + str(d3))
    print('d4: ' + str(d4)) 
    print('d5: ' + str(d5))
    print('d6: ' + str(d6))
    print()
    print("d1.is_leap_year:", d1.is_leap_year())
    print("d2.is_leap_year:", d2.is_leap_year())
    print("d3.is_leap_year()", d3.is_leap_year())
    print("d4.is_leap_year()", d4.is_leap_year())
    print("d5.is_leap_year()", d5.is_leap_year())
    print("d6.is_leap_year()", d6.is_leap_year())
    print()
    print("d1 < d2:", d1<d2)
    print("d2 < d3:", d2<d3)
    print("d3 < d4:", d3<d4)
    print("d4 < d5:", d4<d5)
    print("d5 < d6:", d5<d6)
    
    print ()