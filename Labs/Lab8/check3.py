def get_words(line):
        splitline = line.split('|')
        stringline = splitline[1]
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
    file1 = get_words(file1)
    file2 = get_words(file2)
    same = []
    for i in file1:
        if i in file2:
            same.append(i)

    same = set(same)
    return same


if __name__ == "__main__":
    oneclub = 'csa.txt'
    allclubs = 'allclubs.txt'
    sims = []
    one = open(oneclub)
    oneclubline = one.readline()
    one.close()
    with open(allclubs) as f:
        lines = f.readlines()
        words = get_words(oneclubline)
        for i in lines:
            newwords = get_words(i)
            if newwords != words:
                name = i.split('|')
                sims.append((len(compare(oneclubline, i)),name[0]))
        print(sorted(sims,reverse=True)[:5])