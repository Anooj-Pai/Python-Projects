import statistics

values = [ 14, 10, 8, 19, 7, 13 ]
endval = int(input("Enter a value: "))
print(endval)
values.append(endval)
secnum = int(input("Enter another value: "))
print(secnum)
values.insert(1,secnum)
print(values[3], endval)
values.sort()
diff = values[-1] - values[0]
print("Difference:", diff)
avg = sum(values)/len(values)
print("Average:", round(avg,1))
median = statistics.median(values)
print("Median:", round(median,1))