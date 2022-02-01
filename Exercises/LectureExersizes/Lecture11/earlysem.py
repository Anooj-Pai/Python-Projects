def earlier_semester(sem1,sem2):
    if (int(sem1[1]) > int(sem2[1])):
        return False
    else:
        if (sem1[1] == sem2[1]):
            if sem1[0] == 'Fall':
                return False
            elif sem1[0] == sem2[0]:
                return False
            else:
                return True
        else:
            return True



w1 = ('Spring',2015)
w2 = ('Spring',2014)
w3 = ('Fall', 2014)
w4 = ('Fall', 2015)
print( "{} earlier than {}? {}".format( w1, w2, earlier_semester(w1,w2)))
print( "{} earlier than {}? {}".format( w1, w1, earlier_semester(w1,w1)))
print( "{} earlier than {}? {}".format( w1, w4, earlier_semester(w1,w4)))
print( "{} earlier than {}? {}".format( w4, w1, earlier_semester(w4,w1)))
print( "{} earlier than {}? {}".format( w3, w4, earlier_semester(w3,w4)))
print( "{} earlier than {}? {}".format( w1, w3, earlier_semester(w1,w3)))