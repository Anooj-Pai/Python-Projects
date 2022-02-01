def add(m,n):
    if n == 0:
        return m
    else:
        print('m',m,'n',n)
        return add(m,n-1) + 1
print('Add: ',add(5,3))

print()
def mult(m,n):
    if m < 0 or n < 0:
        return 'Negative Values Invalid'
    elif m == 0 or n == 0:
        return 0
    else:
        print('m',m,'n',n)
        return add(mult(m,n-1),m)
print('Multiply: ', mult(8,3))
print()

''' Original power in terms of mult '''
#def power(x,n):
        #if x < 0 or n < 0:
            #return 'Negative Values Invalid'
        #elif x == 0:
            #return 0
        #elif n == 0:
            #return 1
        #else:
            #print('x',x,'n',n)
            #return mult(power(x,n-1),x)
#print('Power:',power(6,3))
#print(power(6,8))


'''Working Version'''
def power(x,n):
     if x < 0 or n < 0:
        return 'Negative Values Invalid'
     elif x == 0:
        return 0
     elif n == 0:
        return 1
     else:
         return power(x,n-1)*x
print('Power: ', power(6,3))

