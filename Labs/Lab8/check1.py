def parse(file='wrpi.txt'):
    with open(file) as f:
        lines = f.readlines()
        splitline = lines[0].split('|')
        splitline = splitline[1:]
        stringline = splitline[0]
        stringline = stringline.split(' ')

        for i in range(len(stringline)):
            stringline[i] = ''.join(ch for ch in stringline[i] if ch.isalnum())
            stringline[i] = ''.join(ch for ch in stringline[i] if ch.isalpha())

        count = 0
        stringline = set(stringline)
        stringline = list(stringline)

        for i in stringline:
            if len(i) == 0 or len(i) == 1 or len(i) == 2 or len(i) == 3:
                stringline.remove(i)
            else:
                stringline[count] = stringline[count].lower()
            count+=1
        stringline = list(filter(None, stringline))

        count = 0
        for i in stringline:
            if len(i) == 0 or len(i) == 1 or len(i) == 2 or len(i) == 3:
                stringline.remove(i)
            else:
                stringline[count] = stringline[count].lower()
            count+=1

        print(len(set(stringline)), 'words')
        print(set(stringline))


parse()