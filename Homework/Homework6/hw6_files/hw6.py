def parse(file):
    with open(file) as f:
        splitline = []
        lines = f.readlines()
        for line in lines:
            splitline += line.split(' ')
        for i in splitline:
            if '.' in i:
                splitline = splitline[:splitline.index(i) + 1]

        splitline = list(filter(None, splitline))

        for i in range(len(splitline)):
            splitline[i] = ''.join(ch for ch in splitline[i] if ch.isalnum())
            splitline[i] = ''.join(ch for ch in splitline[i] if ch.isalpha())

        splitline = list(filter(None, splitline))

        for i in range(len(splitline)):
            splitline[i] = splitline[i].lower()

        for i in stopwords():
            if i in splitline:
                splitline.remove(i)

        return splitline

def avglen(file):
    avglen = 0
    words = parse(file)
    for i in words:
        avglen += len(i)
    avglen = avglen / len(words)
    print("Evaluating document", file)
    print('1. Average word length: {:.02f}'.format(avglen))

def avglenret(file):
    avglen = 0
    words = parse(file)
    for i in words:
        avglen += len(i)
    avglen = avglen / len(words)
    return avglen


def wordRatio(file):
    total = len(parse(file))
    distinct = len(set(parse(file)))
    print('2. Ratio of distinct words to total words: {:.03f}'.format(distinct / total))


def word_len(file):
    one = []
    two = []
    three = []
    four = []
    five = []
    six = []
    seven = []
    eight = []
    nine = []
    words = parse(file)
    words = set(words)
    words = list(words)
    words.sort()
    for i in words:
        if len(i) == 1:
            one.append(i)
        elif len(i) == 2:
            two.append(i)
        elif len(i) == 3:
            three.append(i)
        elif len(i) == 4:
            four.append(i)
        elif len(i) == 5:
            five.append(i)
        elif len(i) == 6:
            six.append(i)
        elif len(i) == 7:
            seven.append(i)
        elif len(i) == 8:
            eight.append(i)
        elif len(i) == 9:
            nine.append(i)

    print('3. Word sets for document', file + ':')
    if len(one) == 0:
        print('   1:   {}:'.format(len(one)))
    elif len(one) >= 6:
        print('   1:   {}:'.format(len(one)), one[:2],'...',one[-3:])
    else:
        print('   1:   {}:'.format(len(one)), *one)
    if len(two) == 0:
        print('   2:   {}:'.format(len(two)))
    elif len(two) >= 6:
        print('   2:   {}:'.format(len(two)), two[:2],'...',two[-3:])
    else:
        print('   2:   {}:'.format(len(two)), *two)
    if len(three) == 0:
        print('   3:   {}:'.format(len(three)))
    elif len(three) >= 6:
        print('   3:   {}:'.format(len(three)), three[:2],'...',three[-3:])
    else:
        print('   3:   {}:'.format(len(three)), *three)
    if len(four) == 0:
        print('   4:   {}:'.format(len(four)))
    elif len(four) >= 6:
        print('   4:   {}:'.format(len(four)), four[:2],'...',four[-3:])
    else:
        print('   4:   {}:'.format(len(four)), *four)
    if len(five) == 0:
        print('   5:   {}:'.format(len(five)))
    elif len(five) >= 6:
        print('   5:   {}:'.format(len(five)), five[:2],'...',five[-3:])
    else:
        print('   5:   {}:'.format(len(five)), *five)
    if len(six) == 0:
        print('   6:   {}:'.format(len(six)))
    elif len(six) >= 6:
        print('   6:   {}:'.format(len(six)), six[:2],'...',six[-3:])
    else:
        print('   6:   {}:'.format(len(six)), *six)
    if len(seven) == 0:
        print('   7:   {}:'.format(len(seven)))
    elif len(seven) >= 6:
        print('   7:   {}:'.format(len(seven)), seven[:2],'...',seven[-3:])
    else:
        print('   7:   {}:'.format(len(seven)), *seven)
    if len(eight) == 0:
        print('   8:   {}:'.format(len(eight)))
    elif len(eight) >= 6:
        print('   8:   {}:'.format(len(eight)), eight[:2],'...',eight[-3:])
    else:
        print('   8:   {}:'.format(len(eight)), *eight)
    if len(nine) == 0:
        print('   9:   {}:'.format(len(nine)))
    elif len(nine) >= 6:
        print('   9:   {}:'.format(len(nine)), nine[:2],'...',nine[-3:])
    else:
        print('   9:   {}:'.format(len(nine)), *nine)

def word_lencomp(file1, file2):
    one = []
    two = []
    three = []
    four = []
    five = []
    six = []
    seven = []
    eight = []
    nine = []
    words = parse(file1)
    words = set(words)
    words = list(words)
    words.sort()
    for i in words:
        if len(i) == 1:
            one.append(i)
        elif len(i) == 2:
            two.append(i)
        elif len(i) == 3:
            three.append(i)
        elif len(i) == 4:
            four.append(i)
        elif len(i) == 5:
            five.append(i)
        elif len(i) == 6:
            six.append(i)
        elif len(i) == 7:
            seven.append(i)
        elif len(i) == 8:
            eight.append(i)
        elif len(i) == 9:
            nine.append(i)

    one2 = []
    two2 = []
    three2 = []
    four2 = []
    five2 = []
    six2 = []
    seven2 = []
    eight2 = []
    nine2 = []
    words2 = parse(file2)
    words2 = set(words2)
    words2 = list(words2)
    words2.sort()
    for i in words2:
        if len(i) == 1:
            one2.append(i)
        elif len(i) == 2:
            two2.append(i)
        elif len(i) == 3:
            three2.append(i)
        elif len(i) == 4:
            four2.append(i)
        elif len(i) == 5:
            five2.append(i)
        elif len(i) == 6:
            six2.append(i)
        elif len(i) == 7:
            seven2.append(i)
        elif len(i) == 8:
            eight2.append(i)
        elif len(i) == 9:
            nine2.append(i)

    sim1 = 0
    sim2 = 0
    sim3 = 0
    sim4 = 0
    sim5 = 0
    sim6 = 0
    sim7 = 0
    sim8 = 0
    sim9 = 0

    try:
        sim1 = len(set(one) & set(one2)) / float(len(set(one) | set(one2)))
    except ZeroDivisionError:
        pass
    try:
        sim2 = len(set(two) & set(two2)) / float(len(set(two) | set(two2)))
    except ZeroDivisionError:
        pass
    try:
        sim3 = len(set(three) & set(three2)) / float(len(set(three) | set(three2)))
    except ZeroDivisionError:
        pass
    try:
        sim4 = len(set(four) & set(four2)) / float(len(set(four) | set(four2)))
    except ZeroDivisionError:
        pass
    try:
        sim5 = len(set(five) & set(five2)) / float(len(set(five) | set(five2)))
    except ZeroDivisionError:
        pass
    try:
        sim6 = len(set(six) & set(six2)) / float(len(set(six) | set(six2)))
    except ZeroDivisionError:
        pass
    try:
        sim7 = len(set(seven) & set(seven2)) / float(len(set(seven) | set(seven2)))
    except ZeroDivisionError:
        pass
    try:
        sim8 = len(set(eight) & set(eight2)) / float(len(set(eight) | set(eight2)))
    except ZeroDivisionError:
        pass
    try:
        sim9 = len(set(nine) & set(nine2)) / float(len(set(nine) | set(nine2)))
    except ZeroDivisionError:
        pass


    print('   1: {:.04f}'.format(sim1))
    print('   2: {:.04f}'.format(sim2))
    print('   3: {:.04f}'.format(sim3))
    print('   4: {:.04f}'.format(sim4))
    print('   5: {:.04f}'.format(sim5))
    print('   6: {:.04f}'.format(sim6))
    print('   7: {:.04f}'.format(sim7))
    print('   8: {:.04f}'.format(sim8))
    print('   9: {:.04f}'.format(sim9))



def stopwords():
    with open('stop.txt') as f:
        splitline = []
        lines = f.readlines()
        for line in lines:
            splitline += line.split(' ')
        splitline = list(filter(None, splitline))
        for i in range(len(splitline)):
            splitline[i] = ''.join(ch for ch in splitline[i] if ch.isalnum())
            splitline[i] = ''.join(ch for ch in splitline[i] if ch.isalpha())
        splitline = list(filter(None, splitline))
        for i in range(len(splitline)):
            splitline[i] = splitline[i].lower()

        splitline = set(splitline)
        return splitline


def pairs(file):
    words = parse(file)
    tuplist = []
    for i in range(len(words)):
        for j in range(1,max_sep+1):
            try:
                if words[i] != words[i+j]:
                    tuplist.append((words[i],words[i+j]))
            except IndexError:
                pass
    count = 0
    for i in tuplist:
        i = list(i)
        i.sort()
        tuplist[count] = tuple(i)
        count+=1

    fulltuplist = tuplist
    tuplist = set(tuplist)
    tuplist = sorted(tuplist)


    print('4. Word pairs for document', file)
    print('  {} distinct pairs'.format(len(tuplist)))
    if len(tuplist) >= 10:
        print(' ', tuplist[0][0], tuplist[0][1])
        print(' ', tuplist[1][0], tuplist[1][1])
        print(' ', tuplist[2][0], tuplist[2][1])
        print(' ', tuplist[3][0], tuplist[3][1])
        print(' ', tuplist[4][0], tuplist[4][1])
        print('  ...')
        print(' ', tuplist[-5][0], tuplist[-5][1])
        print(' ', tuplist[-4][0], tuplist[-4][1])
        print(' ', tuplist[-3][0], tuplist[-3][1])
        print(' ', tuplist[-2][0], tuplist[-2][1])
        print(' ', tuplist[-1][0], tuplist[-1][1])
    else:
        for i in tuplist:
            print(' ', i[0], i[1])

    print('5. Ratio of distinct word pairs to total: {:.03f}'.format(len(fulltuplist) / len(tuplist)))
    print()

def pairsret(file):
    words = parse(file)
    tuplist = []
    for i in range(len(words)):
        for j in range(1,max_sep+1):
            try:
                if words[i] != words[i+j]:
                    tuplist.append((words[i],words[i+j]))
            except IndexError:
                pass
    count = 0
    for i in tuplist:
        i = list(i)
        i.sort()
        tuplist[count] = tuple(i)
        count+=1

    tuplist = set(tuplist)
    tuplist = sorted(tuplist)
    return tuplist

def analizeFile(file):
    parse(file)
    avglen(file)
    wordRatio(file)
    word_len(file)
    pairs(file)

def compare():
    if avglenret(firstfile) > avglenret(secondfile):
        print('1. {} on average uses longer words than {}'.format(firstfile, secondfile))
    elif avglenret(secondfile) > avglenret(firstfile):
        print('1. {} on average uses longer words than {}'.format(secondfile, firstfile))

    f1words = parse(firstfile)
    f2words = parse(secondfile)
    sim = len(set(f1words) & set(f2words)) / float(len(set(f1words) | set(f2words)))
    print('2. Overall word use similarity: {:.03f}'.format(sim))
    print('3. Word use similarity by length:')
    word_lencomp(firstfile,secondfile)

if __name__ == "__main__":
    firstfile = input("Enter the first file to analyze and compare ==> ")
    print(firstfile)
    secondfile = input("Enter the second file to analyze and compare ==> ")
    print(secondfile)
    max_sep = int(input("Enter the maximum separation between words in a pair ==> "))
    print(max_sep)
    print()
    analizeFile(firstfile)
    analizeFile(secondfile)
    print('Summary comparison')
    compare()
    sim = len(set(pairsret(firstfile)) & set(pairsret(secondfile))) / float(len(set(pairsret(firstfile)) | set(pairsret(secondfile))))
    print('4. Word pair similarity: {:.04f}'.format(sim))
