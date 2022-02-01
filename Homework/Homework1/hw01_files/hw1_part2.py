minutes = input("Minutes ==> ")
print(minutes)
minutes = int(minutes)
seconds = input("Seconds ==> ")
print(seconds)
seconds = int(seconds)
miles = input("Miles ==> ")
print(miles)
miles = float(miles)
targetmiles = input("Target Miles ==> ")
print(targetmiles)
targetmiles = float(targetmiles)
mininsec = minutes*60

paceinsec = (mininsec + seconds) / miles
pace = paceinsec / 60
pacemins = paceinsec / 60
pacesec = int((pace - int(pace)) * 60)
print('')
print("Pace is " + str(int(pacemins)) + " minutes and " + str(pacesec) + " seconds per mile.\r")

mph = miles / (((minutes * 60) + seconds) / 3600)
print("Speed is {:.2f} miles per hour.".format(mph))

targetpace = (paceinsec * targetmiles) / 60
targetpacesec = round(int((targetpace - int(targetpace)) * 60))
targetpacemin = int(targetpace)
print("Time to run the target distance of {:.2f}".format(targetmiles), "miles is "+ str(targetpacemin) + " minutes and", round(targetpacesec),"seconds.")
