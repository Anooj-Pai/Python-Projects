def add_tuples(tuple1,tuple2,tuple3):
    tup1 = tuple1[0]+tuple2[0]+tuple3[0]
    tup2 = tuple1[1]+tuple2[1]+tuple3[1]
    finaltup = (tup1,tup2)
    return(finaltup)

print(add_tuples( (1,4), (8,3), (14,0) ))
print(add_tuples( (3,2), (11,1), (-2,6) ))