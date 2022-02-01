word = input("Enter a string to encode ==> ")
print(word, "\n")
lenword = len(word)
wordenc = ''
wordstart = word

def encrypt(wordenc):
    wordenc = wordenc.replace(" a", "%4%")
    wordenc = wordenc.replace("he", "7!")
    wordenc = wordenc.replace("e", "9(*9(")
    wordenc = wordenc.replace("y", "*%$")
    wordenc = wordenc.replace("u", "@@@")
    wordenc = wordenc.replace("an", "-?")
    wordenc = wordenc.replace("th", "!@+3")
    wordenc = wordenc.replace("o", "7654")
    wordenc = wordenc.replace("9", "2")
    wordenc = wordenc.replace("ck", "%4")
    print("Encrypted as ==>", wordenc)
    print("Difference in length ==>", (len(wordenc)-lenword))
    decrypt(wordenc)

def decrypt(word):
    word = word.replace("%4", "ck")
    word = word.replace("2", "9")
    word = word.replace("7654", "o")
    word = word.replace("!@+3", "th")
    word = word.replace("-?", "an")
    word = word.replace("@@@", "u")
    word = word.replace("*%$", "y")
    word = word.replace("9(*9(", "e")
    word = word.replace("7!", "he")
    word = word.replace("%4%", " a")
    print("Deciphered as ==>", word)
    if word == wordstart:
        print("Operation is reversible on the string.")
    else:
        print("Operation is not reversible on the string.")

encrypt(word)