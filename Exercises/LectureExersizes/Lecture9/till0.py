list = []

init = int(input("Enter a value (0 to end): "))
print(init)
list.append(init)
while init != 0:
    init = int(input("Enter a value (0 to end): "))
    print(init)
    list.append(init)

list.remove(0)
print("Min: ", min(list))
print("Max: ", max(list))
print("Avg: ", round(sum(list)/len(list),1))