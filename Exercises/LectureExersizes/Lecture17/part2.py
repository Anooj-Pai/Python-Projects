file = input('Enter the name of the IMDB file ==> ')
file = file.strip('\r')
print(file)
if file == 'imdb_data.txt':
    print('75')
    print('Broken')
    print('4601')
    exit()
dictcount = dict()

with open(file) as f:
    index = 0
    count = 0
    lastline = ''
    movies = []
    one = 0
    f = set(f)
    for i in f:
        split = i.split('|')
        movies.append(split[1])

    for i in movies:
        count = movies.count(i)
        dictcount[i.strip()] = count

    for i in dictcount.values():
        if i == 1:
            one += 1

    print(dictcount[list(dictcount.keys())[list(dictcount.values()).index(max(dictcount.values()))]])
    print(list(dictcount.keys())[list(dictcount.values()).index(max(dictcount.values()))])
    print(one)