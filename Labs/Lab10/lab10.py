""" 
    This is the skeleton to demonstrate how to put Lab 10 together. 
    It provides an example to show the use of doctest. Note the function,
    addone(x) presented below has an additional 4 lines after 
    the normal function description. The lines beginning with '>>>'
    indicate examples of how the function can be called, and 
    the lines immediately after represent the expected return
    from the call. So, for example, 'addone(1)' should return '2'
    and 'addone(0) should return 1. These lines provide examples
    for a potential user of the lab10 module, but more importantly
    for this lab, they work with the doctest module to allow us to
    do automated testing. 
    
    Look at the file 'test_driver.py' for an example of how to use
    this testing information. Then come back here and change 
    the answer for one or both of the addone examples to 
    an incorrect value and run the testing again to see how a failing
    test is reported.
"""
import time


def closest1(L):
    
    '''
    >>> L1 = [ 15.1, -12.1, 5.4, 11.8, 17.4, 4.3, 6.9 ]
    >>> (x,y) = closest1(L1)
    >>> print(x, y)
    5.4 4.3

    >>> L2 = [ 1.00 ]
    >>> (x,y) = closest1(L2)
    >>> print(x, y)
    None None
    
    >>> Test = [-5 , 13 , 7, -9 , 66 , 88, -49]
    >>> (x,y) = closest1(Test)
    >>> print(x , y)
    -5 -9
    '''
    start = time.time()
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
    
    '''
    >>> L1 = [ 15.1, -12.1, 5.4, 11.8, 17.4, 4.3, 6.9 ]
    >>> (x,y) = closest1(L1)
    >>> print(x, y)
    5.4 4.3

    >>> L2 = [ 1.00 ]
    >>> (x,y) = closest1(L2)
    >>> print(x, y)
    None None
    
    >>> Test = [-5 , 13 , 7, -9 , 66 , 88, -49]
    >>> (x,y) = closest1(Test)
    >>> print(x , y)
    -5 -9
    '''
    start = time.time()
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
    L1 = [ 15.1, -12.1, 5.4, 11.8, 17.4, 4.3, 6.9 ]
    (x,y) = closest2(L1)
    if x > y:
        print(x, y)
    else:
        print(y,x)

    
    L2 = [ 1.00 ]
    (x,y) = closest2(L2)
    print(x, y)

    Test = [-5 , 13 , 7, -9 , 66 , 88, -49]
    (x,y) = closest1(Test)
    if x > y:
        print(x, y)
    else:
        print(y,x)

    pass
    