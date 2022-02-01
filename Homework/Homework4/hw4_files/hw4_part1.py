import hw4_util

global password
password = input("Enter a password => ")
print(password)
global score
score = 0

def lenpass():
    '''This function checks the len of the password with the len function and assigns points accordingly'''
    global score
    if (len(password.strip()) >= 6) and (len(password.strip()) <= 7):
        score += 1
        print("Length: +"+str(1))
    elif len(password.strip()) >= 8 and len(password.strip()) <= 10:
        score += 2
        print("Length: +" + str(2))
    elif len(password.strip()) > 10:
        score += 3
        print("Length: +" + str(3))

def checkupper():
    '''I used the .isupper function to check each letter for its case, then if it was I added it to a counter and once
        each letter was checked I assigned the score based off the counter value.'''
    global score
    uppercount = 0
    for i in range(len(password)):
        if password[i].isupper():
            uppercount +=1
        else: pass
    if uppercount == 1:
        score += 1
        print("Cases: +" + str(1))
    elif uppercount >= 2:
        score += 2
        print("Cases: +" + str(2))

def checkdigit():
    '''I used the .isdigit function to check each character to see if it was a number, then if it was I added it to a counter and once
        each character was checked I assigned the score based off the counter value.'''
    global score
    digitcount = 0
    for i in range(len(password)):
        if password[i].isdigit():
            digitcount += 1
        else:
            pass
    if digitcount == 1:
        score += 1
        print("Digits: +" + str(1))
    elif digitcount >= 2:
        score += 2
        print("Digits: +" + str(2))

def checkspecial():
    '''This function uses simple checks to see if the special characters are in the password then assigns the score accordingly'''
    global score
    if ('!' in password) or ('@' in password) or ('#' in password) or ('$' in password):
        score+=1
        print("!@#$: +" + str(1))
    if ('%' in password) or ('^' in password) or ('&' in password) or ('*' in password):
        score+=1
        print("%^&*: +" + str(1))

def checkplates():
    '''This was the longest function to code. I used a check to make sure there wouldn't be an index out of bounds error.
        Then I used a loop to check the values of the characters and if the case of 3 characters then 4 numbers returned
        true I removed the points.'''
    global score
    password.lower()
    if len(password) > 7:
        for i in range(len(password)):
            if password[i].isalpha():
                if password[i+1].isalpha():
                    if password[i+2].isalpha():
                        if password[i+3].isdigit():
                            if password[i+4].isdigit():
                                if password[i+5].isdigit():
                                    if password[i+6].isdigit():
                                        score -= 2
                                        print("License: -" + str(2))
            else:continue

def checkcommon():
    '''This function pulls the get_top function which gets the list of common passwords.
        I used a loop to look through that list and if there was a match between the passwords then I subtracted the points'''
    global score
    common = hw4_util.part1_get_top()
    for i in range(len(common)):
        if password.strip() == common[i]:
            score-=3
            print("Common: -"+ str(3))
        i+=1
def strength():
    '''This function simply prints the final score then compares it to the cases and prints the strength of it once checked.'''
    global score
    print("Combined score: " + str(score))
    if score <= 0:
        print("Password is rejected")
    if score == 1 or score == 2:
        print("Password is poor")
    if score == 3 or score == 4:
        print("Password is fair")
    if score == 5 or score == 6:
        print("Password is good")
    if score >= 7:
        print("Password is excellent")

def checkpass():
    '''Finally instead of calling all of the functions outside I used this to call all of them in one clean place.'''
    global password
    global score
    lenpass()
    checkupper()
    password = password.lower()
    checkdigit()
    checkspecial()
    checkcommon()
    checkplates()
    strength()

if __name__ == "__main__":
    checkpass()