def get_words(file):
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

        return set(stringline)

def compare(file1, file2):
    f1name = file1
    f2name = file2
    print('Comparing clubs {} and {}:'.format(f1name[:-4], f2name[:-4]))
    file1 = get_words(file1)
    file2 = get_words(file2)
    same = []
    f1diff = []
    f2diff = []

    for i in file1:
        if i in file2:
            same.append(i)
        else:
            f1diff.append(i)
    for i in file2:
        if i in file1:
            same.append(i)
        else:
            f2diff.append(i)

    same = set(same)
    f1diff = set(f1diff)
    f2diff = set(f2diff)

    print('Same words:', same)
    print('Unique to {}:'.format(f1name))
    print(f1diff)
    print('Unique to {}:'.format(f2name))
    print(f2diff)


if __name__ == "__main__":
    compare('wrpi.txt', 'csa.txt')