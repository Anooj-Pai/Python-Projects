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
    


if __name__ == "__main__":
    d1 = Date(1972, 3, 27)
    d2 = Date(1998, 4, 13)
    d3 = Date(1996, 4, 13)
    d4 = Date(1997, 10, 5)
    d5 = Date(1997, 10, 5)
    
    print("d1: " + str(d1))
    print("d2: " + str(d2))
    print("d3: " + str(d3))
    print('d4: ' + str(d4))
    print('d5: ' + str(d5))
    print("d1.same_day_in_year(d2)", d1.same_day_in_year(d2))
    print("d2.same_day_in_year(d3)", d2.same_day_in_year(d3)) 
    print("d3.same_day_in_year(d4)", d3.same_day_in_year(d4))
    print("d4.same_day_in_year(d5)", d4.same_day_in_year(d5))
    print ()