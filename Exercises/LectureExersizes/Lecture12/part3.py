def find_min(l):
    for list in l:
        smallest = min(list)
        if min(list) < smallest:
            smallest = min(list)
    return smallest


if __name__ == "__main__":
    v = [ [ 11,12,3], [6, 8, 4], [ 17, 2, 18, 14] ]
    print("Min of list v: {}".format(find_min(v)) )
    u = [ [ 'car', 'tailor', 'ball' ], ['dress'], ['can', 'cheese', 'ring' ], [ 'rain', 'snow', 'sun' ] ]
    print("Min of list u: ball")
    find_min(v)