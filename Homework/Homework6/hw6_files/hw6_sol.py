'''This function takes a file and gets all of the words, then strips the non alpha
characters then removes the stop words and returns a list of the words'''
def parse(file, stop='stop.txt'):
    array = []
    stop_array = []
    new_array = []

    with open(stop) as s:
        sread = s.readlines()
        for i in sread:
            stopper = i.strip().split()
            stop_array.append(stopper)

    with open(file) as f:
        read = f.readlines()
        for i in read:
            string = read.split()
        for i in string:
            line = ''
            if (i.isalpha() == True):  # checks if it is an alphabet.
                array.append(i.lower())
            else:
                for char in i:
                    if char.isalpha() == True:
                        line = line + char.lower()
                array.append(line.strip())

        for x in stopper:
            line = ''
            if (x.isalpha() == True):
                stop_array.append(x.lower())
            else:
                for cha in x:
                    if cha.isalpha() == True:
                        line = line + cha.lower()
                stop_array.append(line.strip())

        for index in array:
            if index == '':
                array.remove(index)

        for value in array:
            if value not in stop_array: #checks if word is in stop list
                new_array.append(value)

    return new_array

'''This function gets the len of each word then gets the average len'''
def avglen(file):
    avglen = 0
    words = parse(file)
    for i in words:
        avglen += len(i) #gets all the lens
    avglen = avglen / len(words) #gets avg
    print("Evaluating document", file)
    print('1. Average word length: {:.02f}'.format(avglen))

'''Same function just returns the value'''
def avglenret(file):
    avglen = 0
    words = parse(file)
    for i in words:
        avglen += len(i)
    avglen = avglen / len(words)
    return avglen

'''calculates the distinct word ratio by getting the total words then using a set to
get rid of duplicates. Then it gets the ratio of the 2.'''
def wordRatio(file):
    total = len(parse(file))
    distinct = len(set(parse(file)))
    print('2. Ratio of distinct words to total words: {:.03f}'.format(distinct / total))

'''This function takes the list of words and creates a new list of sets
for each len of words'''
def wordset(lst):
    array = []
    new = []
    for i in lst:
        array.append(len(i))
    Max = max(array) + 1

    for j in range(Max):
        Set = set()
        new.append(Set)

    for index in range(len(new)):
        for word in range(len(lst)):
            if index == len(lst[word]):
                new[index].add(lst[word])
    return new

'''Uses the wordset function and prints the words in the correct line based off len'''
def word_len(file):
    print('3. Word sets for document {}:'.format(file))
    new = wordset(parse(file))
    for i in range(1,len(new)):#for loop for each len
        num = len(new[i])
        lst = list(new[i])
        lst.sort()
        line =' '
        for word in lst:
            line += word+' '
        if num > 6: #incase there are more than 6 words
            List = line.split()
            sentence = ' ' + List[0]+' ' +  List[1]+' '  +List[2]+' ... '+ List[-3]+' '+ List[-2]+' '+ List[-1]
            line = sentence
        if num < 6:
            line = line[:-1]
        elif num == 0:
            line = ''

        if i < 10:#checks for formatting
            if num > 9:
                print('   {}:  {}:{}'.format(i,num,line))
            else:
                print('   {}:   {}:{}'.format(i,num,line))
        else:
            if num > 9:
                print('  {}:  {}:{}'.format(i,num,line))
            else:
                print('  {}:   {}:{}'.format(i,num,line))

'''A very, very, very, long and terribly inefficent function that calculates the len simlarity 
of each len of words between the 2 files'''
def word_lencomp(file1, file2):
    #lists for each len
    one = []
    two = []
    three = []
    four = []
    five = []
    six = []
    seven = []
    eight = []
    nine = []
    ten = []
    eleven = []
    twelve = []
    thirteen = []
    fourteen = []
    words = parse(file1)
    words = set(words)
    words = list(words)
    words.sort()
    wordslen = []
    for i in words:#creates a list of lens
        wordslen.append(len(i))
    for i in words:#adds words to len lists
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
        elif len(i) == 10:
            ten.append(i)
        elif len(i) == 11:
            eleven.append(i)
        elif len(i) == 12:
            twelve.append(i)
        elif len(i) == 13:
            thirteen.append(i)
        elif len(i) == 14:
            fourteen.append(i)
    #repeats for second file
    one2 = []
    two2 = []
    three2 = []
    four2 = []
    five2 = []
    six2 = []
    seven2 = []
    eight2 = []
    nine2 = []
    ten2 = []
    eleven2 = []
    twelve2 = []
    thirteen2 = []
    fourteen2 = []
    words2 = parse(file2)
    words2 = set(words2)
    words2 = list(words2)
    words2.sort()
    words2len = []
    for i in words2:
        words2len.append(len(i))
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
        elif len(i) == 10:
            ten2.append(i)
        elif len(i) == 11:
            eleven2.append(i)
        elif len(i) == 12:
            twelve2.append(i)
        elif len(i) == 13:
            thirteen2.append(i)
        elif len(i) == 14:
            fourteen2.append(i)

    #trys each sim val formula and sets to 0 if no values
    try:
        sim1 = len(set(one) & set(one2)) / float(len(set(one) | set(one2)))
    except ZeroDivisionError:
        sim1 = 0
    try:
        sim2 = len(set(two) & set(two2)) / float(len(set(two) | set(two2)))
    except ZeroDivisionError:
        sim2 = 0
    try:
        sim3 = len(set(three) & set(three2)) / float(len(set(three) | set(three2)))
    except ZeroDivisionError:
        sim3 = 0
    try:
        sim4 = len(set(four) & set(four2)) / float(len(set(four) | set(four2)))
    except ZeroDivisionError:
        sim4 = 0
    try:
        sim5 = len(set(five) & set(five2)) / float(len(set(five) | set(five2)))
    except ZeroDivisionError:
        sim5 = 0
    try:
        sim6 = len(set(six) & set(six2)) / float(len(set(six) | set(six2)))
    except ZeroDivisionError:
        sim6 = 0
    try:
        sim7 = len(set(seven) & set(seven2)) / float(len(set(seven) | set(seven2)))
    except ZeroDivisionError:
        sim7 = 0
    try:
        sim8 = len(set(eight) & set(eight2)) / float(len(set(eight) | set(eight2)))
    except ZeroDivisionError:
        sim8 = 0
    try:
        sim9 = len(set(nine) & set(nine2)) / float(len(set(nine) | set(nine2)))
    except ZeroDivisionError:
        sim9 = 0
    try:
        sim10 = len(set(ten) & set(ten2)) / float(len(set(ten) | set(ten2)))
    except ZeroDivisionError:
        sim10 = 0
    try:
        sim11 = len(set(eleven) & set(eleven2)) / float(len(set(eleven) | set(eleven2)))
    except ZeroDivisionError:
        sim11 = 0
    try:
        sim12 = len(set(twelve) & set(twelve2)) / float(len(set(twelve) | set(twelve2)))
    except ZeroDivisionError:
        sim12 = 0
    try:
        sim13 = len(set(thirteen) & set(thirteen2)) / float(len(set(thirteen) | set(thirteen2)))
    except ZeroDivisionError:
        sim13 = 0
    try:
        sim14 = len(set(fourteen) & set(fourteen2)) / float(len(set(fourteen) | set(fourteen2)))
    except ZeroDivisionError:
        sim14 = 0

    #checks the greatest len and prints all the sim vals for each len
    if max(wordslen) > max(words2len):
        for i in range(1, max(wordslen)+1):
            if i == 1:
                print('   {}: {:.04f}'.format(i, sim1))
            elif i == 2:
                print('   {}: {:.04f}'.format(i, sim2))
            elif i == 3:
                print('   {}: {:.04f}'.format(i, sim3))
            elif i == 4:
                print('   {}: {:.04f}'.format(i, sim4))
            elif i == 5:
                print('   {}: {:.04f}'.format(i, sim5))
            elif i == 6:
                print('   {}: {:.04f}'.format(i, sim6))
            elif i == 7:
                print('   {}: {:.04f}'.format(i, sim7))
            elif i == 8:
                print('   {}: {:.04f}'.format(i, sim8))
            elif i == 9:
                print('   {}: {:.04f}'.format(i, sim9))
            elif i == 10:
                print('  {}: {:.04f}'.format(i, sim10))
            elif i == 11:
                print('  {}: {:.04f}'.format(i, sim11))
            elif i == 12:
                print('  {}: {:.04f}'.format(i, sim12))
            elif i == 13:
                print('  {}: {:.04f}'.format(i, sim13))
            elif i == 14:
                print('  {}: {:.04f}'.format(i, sim14))
    else:
        for i in range(1, max(words2len)+1):
            if i == 1:
                print('   {}: {:.04f}'.format(i, sim1))
            elif i == 2:
                print('   {}: {:.04f}'.format(i, sim2))
            elif i == 3:
                print('   {}: {:.04f}'.format(i, sim3))
            elif i == 4:
                print('   {}: {:.04f}'.format(i, sim4))
            elif i == 5:
                print('   {}: {:.04f}'.format(i, sim5))
            elif i == 6:
                print('   {}: {:.04f}'.format(i, sim6))
            elif i == 7:
                print('   {}: {:.04f}'.format(i, sim7))
            elif i == 8:
                print('   {}: {:.04f}'.format(i, sim8))
            elif i == 9:
                print('   {}: {:.04f}'.format(i, sim9))
            elif i == 10:
                print('  {}: {:.04f}'.format(i, sim10))
            elif i == 11:
                print('  {}: {:.04f}'.format(i, sim11))
            elif i == 12:
                print('  {}: {:.04f}'.format(i, sim12))
            elif i == 13:
                print('  {}: {:.04f}'.format(i, sim13))
            elif i == 14:
                print('  {}: {:.04f}'.format(i, sim14))

'''Takes the words for each file and finds all of the pairs'''
def pairs(file):
    words = parse(file)
    tuplist = []
    count = 0
    for i in range(len(words)):
        for j in range(1, max_sep + 1):#checks the values up until max sep
            if not (i + j >= len(words)):
                if words[i] < words[i + j]:
                    tple = words[i], words[i + j]
                else:
                    tple = words[i + j], words[i]
                count += 1
                tuplist.append(tple)

    tuplist = set(tuplist)
    tuplist = sorted(tuplist)
    #prints all of the pairs
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

'''calculates the ratio of the distinct pairs vs total'''
def pairratio(file):
    ratio = (len(set(pairsret(file)))) / (len(pairsret(file)))
    print('5. Ratio of distinct word pairs to total: {:.03f}'.format(ratio))
    print()

'''same function just returns the list instead of printing'''
def pairsret(file):
    words = parse(file)
    tuplist = []
    count = 0
    for i in range(len(words)):
        for s in range(1, max_sep + 1):
            if not (i + s >= len(words)):

                if words[i] < words[i + s]:
                    tple = words[i], words[i + s]
                else:
                    tple = words[i + s], words[i]
                count += 1
                tuplist.append(tple)

    return tuplist

'''calls all of the functions'''
def analizeFile(file):
    parse(file)
    avglen(file)
    wordRatio(file)
    word_len(file)
    pairs(file)
    pairratio(file)

'''function that compares all areas of the 2 files'''
def compare():
    if avglenret(firstfile) > avglenret(secondfile):#checks avg len for both
        print('1. {} on average uses longer words than {}'.format(firstfile, secondfile))
    elif avglenret(secondfile) > avglenret(firstfile):
        print('1. {} on average uses longer words than {}'.format(secondfile, firstfile))

    f1words = parse(firstfile)
    f2words = parse(secondfile)
    #checks word similarity
    sim = len(set(f1words) & set(f2words)) / float(len(set(f1words) | set(f2words)))
    print('2. Overall word use similarity: {:.03f}'.format(sim))
    #calls the really long function to compare each by len
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