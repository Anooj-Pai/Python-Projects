from syllables import find_num_syllables

#inputs
paragraph = input("Enter a paragraph => ")
print(paragraph)
parlist = paragraph.split()

#calculate the hard words
def PHW():
    hard = []
    for i in parlist:
        if (find_num_syllables(i) >= 3) and (('-' in i) == False):
            hard.append(i)
        else:pass
    return(hard)

#calculates the % of hard words
def PHWPER():
    hard = []
    for i in parlist:
        if (find_num_syllables(i) >= 3) and (('-' in i) == False):
            hard.append(i)
        else:pass
    percent = (len(hard)/len(parlist))*100
    return(float(percent))

#calculates the average words per sentence
def ASL():
    words = []
    sentences = paragraph.split('.')
    for i in (range(len(sentences)-1)):
        sent = sentences[i].split()
        length = len(sent)
        words.append(length)
    avg = sum(words)/len(words)
    return(float(avg))

#calculates the average words per sentence
def ASYL():
    syllables = []
    sentences = paragraph.split('.')
    for i in (range(len(sentences)-1)):
        sent = sentences[i].split()
        for i in range(len(sent)):
            syllable = find_num_syllables(sent[i])
            syllables.append(syllable)
    avg = sum(syllables)/len(syllables)
    return(float(avg))

#calculates the GFRI thing
def GFRI():
    tot = ASL()+PHWPER()
    return(0.4*tot)

#calculates the FKRI thing
def FKRI():
    ans = float(206.835-1.015*ASL()-86.4*ASYL())
    return(ans)

#prints everything and formats it
print("Here are the hard words in this paragraph:\n", PHW())
print("Statistics: ASL:{:.02f}".format(ASL()), "PHW:{:.02f}".format(PHWPER()) + "%", "ASYL:{:.02f}".format(ASYL()))
print("Readability index (GFRI): {:.02f}".format(GFRI()))
print("Readability index (FKRI): {:.02f}".format(FKRI()))