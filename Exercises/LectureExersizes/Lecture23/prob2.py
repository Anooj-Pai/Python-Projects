
def fib(n):
    if n == 0:
        return (n)
    elif n == 1 or n== 2:
        return 1
    else:
        return fib(n-1)+fib(n-2)


if __name__ == "__main__":
    print( fib(0) )
    print( fib(1) )
    print( fib(2) )
    print( fib(5) )
    print( fib(10) )
