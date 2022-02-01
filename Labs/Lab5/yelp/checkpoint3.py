import lab05_util
import webbrowser

rests = lab05_util.read_yelp('yelp.txt')

def print_info(num):
    current = rests[num]
    addy = current[3].split('+')
    print(current[0] + " (" + current[5] + ")")
    print('\t' + addy[0])
    print('\t' + addy[1])
    score = sum(current[-1])/len(current[-1])
    if score >= 0 and score < 2:
        print("This restaurant is rated bad, based on {} reviews.".format(len(current[-1])))
    elif score >= 2 and score < 3:
        print("This restaurant is rated average, based on {} reviews.".format(len(current[-1])))
    elif score >= 3 and score < 4:
        print("This restaurant is rated above average, based on {} reviews.".format(len(current[-1])))
    elif score >= 4 and score <= 5:
        print("This restaurant is rated very good, based on {} reviews.".format(len(current[-1])))
    next = int(input("What would you like to do next?   \n1. Visit the homepage \n2. Show on Google Maps \n3. Show directions to this restaurant \nYour choice (1-3)? ==>"))
    if next == 1:
        webbrowser.open(current[4])
    elif next == 2:
        webbrowser.open('http://www.google.com/maps/place/' + current[3])
    elif next == 3:
        webbrowser.open('http://www.google.com/maps/dir/110+8th+Street,+Troy+NY/' + current[3])

while True:
    rest = int(input("Enter an id for a restaurant: "))
    rest -= 1
    if rest < 0:
        print("ID out of range")
        exit()
    elif rest > len(rests):
        print("ID out of range")
        exit()
    print_info(rest)