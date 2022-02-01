'''
Template program for Lecture 20 exercises.
'''
def modlinear_search(x, L):
    if x in L:
        return L.index(x)
    else:
        for i in L:
            if x > i:
                pass
            else:
                if L.index(i) == len(L)-1:
                    return len(L)
                else:
                    return L.index(i)
    return len(L)


if __name__ == "__main__":
    #  Get the name of the file containing data
    fname = input('Enter the name of the data file => ')
    print(fname)

    #  Open and read the data values
    in_file = open(fname,'r')
    values = []
    for line in in_file:
        v = float(line)
        values.append(v)

    #  Search for each value requested by the user until -1 is entered
    x = 0
    while x != -1:
        x = float(input("Enter a value to search for ==> "))
        print(x)
        if x != -1:
            loc = modlinear_search(x, values )
            print(loc)
