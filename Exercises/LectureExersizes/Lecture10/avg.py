co2_levels = [ 320.03, 322.16, 328.07, 333.91, 341.47, \
               348.92, 357.29, 363.77, 371.51, 382.47, 392.95 ]

average = sum(co2_levels)/len(co2_levels)
count = 0
for i in co2_levels:
    if i > average:
        count += 1
    else:
        pass
    i += 1

print("Average:", round(average,2))
print("Num above average:", count)