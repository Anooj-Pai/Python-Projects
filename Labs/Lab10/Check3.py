import random
from time import time
def closest1(L):
    temp = abs(max(L) - min(L))
    if len(L) > 1:
        for i in range(len(L)):
            for j in range(len(L)):
                if i == j:
                    continue
                if abs(L[i] - L[j]) < temp:
                    temp = abs(L[i] - L[j])
                    cord = L[i] , L[j]
        return cord
    else:
        return (None, None)
    
def closest2(L):
    if len(L) > 1:
        temp = L.copy()
        temp.sort()
        dist = abs(temp[0] - temp[1])
        for i in range(len(temp) - 1):
            if abs(temp[i] - temp[i + 1]) < dist:
                dist = abs(temp[i] - temp[i + 1])
                cord = temp[i] , temp[i + 1]

        return cord
    else:
        return (None, None)
            
if __name__ == "__main__":
    n = int(input('Size of List: '))
    L = []
    for i in range(n):
        r = random.uniform(0.0, n)
        L.append(r)
    
    t0 = time()
    (x,y) = closest1(L)
    print( x, y )
    t1 = time()
    (x,y) = closest2(L)
    print( x, y )
    t2 = time()
    print("--- %s seconds ---" % (t1 - t0))
    print("--- %s seconds ---" % (t2 - t1))
