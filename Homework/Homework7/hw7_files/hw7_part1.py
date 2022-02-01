'''This function parses through the dict file and puts the words and freq in a dict'''
def dictparse(file):
    wordsdict = dict()
    with open(file) as f:
        for line in f:
            split = line.split(',')
            split[1] = split[1].strip('\n')
            wordsdict[split[0]] = split[1]
    return(wordsdict)

'''This funtion parses through the keyboard file and puts the first letter as the key and the others as the
value in a dict'''
def kbparse(file):
    letterdict = dict()
    with open(file) as f:
        for line in f:
            split = line.split(' ')
            split[-1] = split[-1].strip('\n')
            letterdict[split[0]] = split[1:]
    return(letterdict)

'''This function checks if the word is in the dict and if it is adds Found to the values'''
def wordcheck(word):
    dict = dictparse(dictfile)
    if word in dict:
        templist.append('Found')
    else:
        return

'''This function goes through each letter in the word and drops it
then it checks if that word is in the dict and returns it if it is'''
def drop(word):
    dict = dictparse(dictfile)
    for i in range(len(word)):
        cut = word[:i]+word[i+1:]
        if cut in dict:
            templist.append(cut)
        else:
            pass

'''This funtion parses through the letters in the word and adds every letter
into it to see if it can make a word that is in the dict'''
def insert(word):
    dict = dictparse(dictfile)
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    ogword = word
    for i in range(len(word)+1):
        for j in alphabet:
            word = word[:i] + j + word[i:]
            if word in dict:
                templist.append(word)
                word = ogword
            else:
                word = ogword

'''This function swaps the letter the loop is on and the next one
then checks if it is in the dict'''
def swap(word):
    dict = dictparse(dictfile)
    try:
        for i in range(len(word)):
            c = list(word)
            c[i], c[i+1] = c[i+1], c[i]
            tempword = ''.join(c)
            if tempword in dict:
                templist.append(tempword)
    except IndexError:
        pass

'''This replaces each letter with one of the frequently mistyped letters
from the keyboard file then checks if it is in the dict'''
def replace(word):
    dict = dictparse(dictfile)
    letters = kbparse(kbfile)
    ogword = word
    for i in range(len(word)):
        if word[i] in letters:
            for j in letters[word[i]]:
                word = list(word)
                word[i] = j
                word = ''.join(word)
                if word in dict:
                    templist.append(word)
                else:
                    word = ogword

'''This function formats the word and words into the line'''
def format(word):
        try:
            if 'Found' in worddict[word]: #if its in the dict then just print found
                print('{} -> FOUND'.format(' ' * (15-len(word))+word))
            elif worddict[word] != []: #if it is found with changes
                dictwords = dictparse(dictfile)
                newlist = []
                for i in templist:
                    newlist.append((float(dictwords[i]), i))#creates tuples with frequ to sort
                newlist.sort(reverse=True) #sorts
                if len(newlist) > 3: #prints the top 3
                    newlist = newlist[:3]
                flist = ''
                for i in newlist: #puts the words into a string to print
                    flist += i[1] + ' '
                flist = flist.rstrip()
                if len(templist) < 10:
                    print('{} -> FOUND  {}:  {}'.format(' ' * (15-len(word))+word, len(templist), flist))
                else:
                    print('{} -> FOUND {}:  {}'.format(' ' * (15 - len(word))+word, len(templist), flist))
            else:
                print('{} -> NOT FOUND'.format(' ' * (15-len(word))+word))
        except KeyError:
            pass

'''All of the function calling and inputs'''
if __name__ == '__main__':
    worddict = dict()
    dictfile = input('Dictionary file => ').strip()
    print(dictfile)
    inputfile = input('Input file => ').strip()
    print(inputfile)
    kbfile = input('Keyboard file => ').strip()
    print(kbfile)

    with open(inputfile) as f:
        for word in f:
            templist = []
            word = word.strip()
            word = word.strip('\n')
            #calls all of the test funcs
            templist.append(wordcheck(word))
            templist.append(drop(word))
            templist.append(insert(word))
            templist.append(swap(word))
            templist.append(replace(word))
            while None in templist:
                templist.remove(None)
            templist = set(templist)
            templist = list(templist)
            worddict[word] = templist
            format(word)

