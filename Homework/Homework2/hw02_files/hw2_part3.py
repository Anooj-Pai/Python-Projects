sentence = input("Enter a sentence => ")
print(sentence)
sentence = sentence.lower()
happycount = 0
sadcount = 0

def number_happy(sentence):
    global happycount
    happycount += sentence.count("laugh")
    happycount += sentence.count("happiness")
    happycount += sentence.count("love")
    happycount += sentence.count("excellent")
    happycount += sentence.count("good")
    happycount += sentence.count("smile")
    number_sad(sentence)

def number_sad(sentence):
    global sadcount
    sadcount += sentence.count("bad")
    sadcount += sentence.count("sad")
    sadcount += sentence.count("terrible")
    sadcount += sentence.count("horrible")
    sadcount += sentence.count("problem")
    sadcount += sentence.count("hate")
    print("Sentiment:",'+'*happycount + '-'*sadcount)
    if happycount > sadcount:
        print("This is a happy sentence.")
    elif sadcount > happycount:
        print("This is a sad sentence.")
    else:
        print("This is a neutral sentence.")

number_happy(sentence)