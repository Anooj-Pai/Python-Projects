#Parsing so only actual words are in the list. no numbers or odd symbols
def splitter(doc,stop):
    s = open(stop,'r')
    new_array = []
    sread = s.read()
    stopper = sread.strip().split()
    array = []
    stop_array = []
    file = open(doc,'r')
    read = file.read()
    string = read.strip().split()
    for i in string:
            line = ''
            if (i.isalpha() == True): #checks if it is an alphabet.
                array.append(i.lower())
            else: 
                for char in i:
                    
                    if char.isalpha() == True:
                        line = line + char.lower()
                array.append(line.strip())
                
    for x in stopper:
            line = ''
            if (x.isalpha() == True): #checks if it is an alphabet.
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
        if value not in stop_array:
            new_array.append(value)
    return new_array



#calculates average word length of list
def avg_length(lst):
    count = 0
    length = 0
    for i in lst:
        length += len(i)
        count+=1
    return '{:.2f}'.format(float(length)/float(count))
    
#calculates the ratio
def ratio(i):
    length = len(set(i))
    length2= len(i)
    return length/length2

def ltos(lst):
    array = []
    new = []
    for i in lst:
        array.append(len(i))
    Max = max(array)+1

    for j in range(Max):
        Set = set()
        new.append(Set)
    
    for index in range(len(new)):
        for word in range(len(lst)):
            if index == len(lst[word]):
                new[index].add(lst[word])
    return new
    
    
#prints number of words and their lengths and similarities
def output(new):
    for i in range(1,len(new)):
        num = len(new[i])
        lst = list(new[i])
        lst.sort()
        line =''
        for word in lst:
            line += word+ ' '
        if num > 6:
            List = line.split()
            sentence = List[0]+' ' +  List[1]+' '  +List[2]+' ... '\
                + List[-3]+' '+ List[-2]+' '+ List[-1]+' '
            line = sentence
        print('{}:   {}: {}'.format(i,num,line))
        
        
#prints pairs of words that are near eachother by max_sep
def distinct_pairs(lst,sep):
    array = []
    count = 0
    for i in range(len(lst)):
        for s in range(1,sep+1):
            if not(i + s >=  len(lst)):
           
                if lst[i] < lst[i+s]:
                    tple = lst[i],lst[i+s]
                else:
                    tple = lst[i+s],lst[i]
                count+=1   
                array.append(tple) 
                #count is giving 1 extra than it should be.
    return array



#part 4 program work

def distinct_pairs_final(file,stop,sep):
    List = distinct_pairs(splitter(file,stop),sep)
    List = set(List)
    List = list(List)
    List.sort()
    print("Word pairs for document {}".format(file))
    print("{} distinct pairs".format(len(List)))
    
   
    if len(List) >= 10:
        for x in range(5):
            print("{} {}".format(List[x][0],List[x][1]))
        print("...")
        for y in range(-5,0):
            print("{} {}".format(List[y][0],List[y][1]))
    else:      
        for j in List:  
            print("{} {}".format(j[0],j[1]))    
                                                 

def ratio2(file,stop,sep):   
    ratio= (len(set(distinct_pairs(splitter(file,stop),sep))))/(len(distinct_pairs(splitter(file,stop),sep)))
    return ratio

def similarity(doc1,doc2,stop):
    a = set(splitter(doc1,stop)).union(set(splitter(doc2,stop)))
    b =set(splitter(doc1,stop)).intersection(set(splitter(doc2,stop)))
    return len(b)/len(a)
    
def similar_ltos(ltos1,ltos2):
    x = len(ltos1)
    y = len(ltos2)
    index = 0
    if x > y:
        diff = x-y
        while index < diff:
            ltos2.append(set())
            index+=1
    else: 
        diff = y -x 
        while index < diff:
            ltos1.append(set())
            index+=1
            
    for i in range(len(ltos1)):
        if ltos1[i] != set() and ltos2[i] != set():
            union = ltos1[i].union(ltos2[i])
            intersection = ltos1[i].intersection(ltos2[i])
            similar = len(intersection)/len(union)
            print("{}: {:.4f}".format(i,similar))
        else: print("{}: {:.4f}".format(i,0.0000))
            
def word_pair_similarity(doc1,doc2,stop,sep):
    union = set(distinct_pairs(splitter(doc1,stop),sep)).union(set(distinct_pairs(splitter(doc2,stop),sep)))
    intersection = set(distinct_pairs(splitter(doc1,stop),sep)).intersection(set(distinct_pairs(splitter(doc2,stop),sep)))
    s = len(intersection)/len(union)
    return s
if __name__ == "__main__":
    stop = 'stop.txt'
    doc1 = input("Enter the first file to analyze and compare ==> ")
    print(doc1)
    doc2= input("Enter the second file to analyze and compare ==> ")
    print(doc2)
    n = input("Enter the maximum separation between words in a pair ==> ")
    print(n)
    n = int(n)
    
    print("Evaluating document {}".format(doc1))
    print("1. Average word length: {}".format(avg_length(splitter(doc1,stop))))
    print("2. Ratio of distinct words to total words: {:.3f}".format(ratio(splitter(doc1,stop))))
    print("3. Word sets for document {}:".format(doc1))
    (output(ltos(splitter(doc1,stop))))
    print("4. Word pairs for document {}:".format(doc1))
    distinct_pairs_final(doc1,stop,n)
    print("5. Ratio of distinct pairs to total: {}".format(ratio2(doc1,stop,n)))
   # spaces * 4 - len(string)
    print()
    print("Evaluating document {}".format(doc2))
    print("1. Average word length: {}".format(avg_length(splitter(doc2,stop))))
    print("2. Ratio of distinct words to total words: {:.3f}".format(ratio(splitter(doc2,stop))))
    print("3. Word sets for document {}:".format(doc2))
    (output(ltos(splitter(doc2,stop))))
    print("4. Word pairs for document {}:".format(doc2))
    distinct_pairs_final(doc2,stop,n)
    print("5. Ratio of distinct word pairs to total: {:.3f}".format(ratio2(doc2,stop,n)))
    print()
    #avg word length
    print("Summary comparison")
    if (avg_length(splitter(doc1,stop)) > avg_length(splitter(doc2,stop))):
        print("{} on average uses longer words than {}".format(doc1,doc2))
    else:
        print("{} on average uses longer words than {}".format(doc2,doc1))
    print("Overall word use similarity: {:.3f}".format(similarity(doc1,doc2,stop)))
    print("Word use similarity by length:")
    similar_ltos(ltos(splitter(doc1,stop)),ltos(splitter(doc2,stop)))
    print('4. Word pair similarity: {:.4f}'.format(word_pair_similarity(doc1,doc2,stop,n)))
    