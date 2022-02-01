census = [ 340, 589, 959, 1372, 1918, 2428, 3097, 3880, 4382, 5082, \
            5997, 7268, 9113, 10385, 12588, 13479, 14830, 16782, \
            8236, 17558, 17990, 18976, 19378 ]

avglist = []

i = 0
smallavg = (census[i+1]-census[i])/census[i]*100
avglist.append(smallavg)
i = 2
while i < len(census)-1:
    smallavg = (census[i]-census[i-1])/census[i-1]*100
    avglist.append(smallavg)
    i+=1

print("Average = " + str((round(sum(avglist)/len(avglist),1))-1)+"%")