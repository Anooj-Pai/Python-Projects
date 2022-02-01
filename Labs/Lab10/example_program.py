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
    start = time.time()
    minn = 100
    for i in range(len(L)):
        for j in range(len(L)):
            diff = L[i] - L[j]
            diff2 = L[j] - L[i]
            if i != j:
                if diff < minn and diff > 0:
                    temptup = (L[i], L[j])
                    minn = L[i] - L[j]
                elif diff2 < minn and diff2 > 0:
                    temptup = (L[j], L[j])
                    minn = L[j] - L[i]
                else:pass
    end = time.time()
    print("Time for method 1:", end-start)

    '''
    >>> closest1([1,2,5,8,19])
    (2,1)
    '''
    return temptup

def closest2(L):
    start = time.time()
    L.sort()
    minn = 100
    temptup = ()
    if len(L) < 2:
        return (None, None)
    for i in range(len(L)):
        try:
            diff = L[i] - L[i+1]
            diff2 = L[i+1] - L[i]
            if diff < minn and diff > 0:
                temptup = (L[i], L[i+1])
                minn = diff
            elif diff2 < minn and diff2 > 0:
                temptup = (L[i+1], L[i])
                minn = diff2
            else:
                pass
        except IndexError:
            break
    end = time.time()
    print("Time for method 2:", end - start)
    return temptup

if __name__ == "__main__":
    pass
