import math
#inputs
bears = int(input("Number of bears => "))
print(bears)
tourists = 0
berries = input("Size of berry area => ")
print(berries)
berries = float(berries)
berries = int(berries)

bearlist = [bears]
berrylist = [berries]
tourlist = []
#find the num of tourists
def numtour(bears):
    if bears < 4 or bears > 15:
        tourists = 0
    else:
        if bears <= 10:
            tourists = bears*10000
        elif bears > 10:
            tourists = ((bears-10)*20000)+(100000)
    tourlist.append(tourists)
    return tourists

#find the num of bears
def numbears(bears, berries, tourists):
    bears_next = berries / (50 * (bears + 1)) + bears * 0.60 - (math.log(1 + tourists, 10) * 0.1)
    return max([0,bears_next])

#find the num of berries
def numberry(bears, berries, tourists):
    berries_next = (berries * 1.5) - (bears + 1) * (berries / 14) - (math.log(1 + tourists, 10) * 0.05)
    return max([0,berries_next])

#the main func to find all for 10 years
def find_next(bears, berries, tourists):
    print("Year      Bears     Berry     Tourists  ")
    print("1         " + str(bears) + "         {:.01f}".format(berries) + "     " + str(tourists) + "  ")
    for i in range(2,11):
        bear = int(numbears(bears, berries, tourists))
        berry = numberry(bears, berries, tourists)
        tourist = numtour(bear)
        print(str(i) + " "*(10-len(str(i))) + str(int(bear))+" "*(10 - len(str(int(bear)))) + "{:.01f}".format(berry)+" "*(10 - len(str(float(round(berries,1)))))+str(int(tourist))+" "*(10 - len(str(int(tourist)))))
        bears = bear
        berries = berry
        tourists = tourist
        bearlist.append(bears)
        berrylist.append(berries)
        tourlist.append(tourists)

find_next(bears, berries,numtour(bears))
#printing the min and max
print('\r')
print("Min:      " + str(min(bearlist)) + "         {:.01f}".format(min(berrylist)) + "     " + str(min(tourlist)) + "         ")
print("Max:      " + str(max(bearlist)) + "         {:.01f}".format(max(berrylist)) + "     " + str(max(tourlist)) + "         ")