
def fib(n):
    if n == 0:
        return 0
    else:
        val1,val2 = 1,1
        while n > 2:
            val1,val2 = val2,val1+val2
            n-=1
        return val2

if __name__ == "__main__":
    print( fib(0) )
    print( fib(1) )
    print( fib(2) )
    print( fib(5) )
    print( fib(10) )
