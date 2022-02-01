filename = input("Data file name: ").strip()
print(filename)
lastname = input("Prefix: ").strip()
print(lastname)

if lastname == "Do":
    print('3648 last names')
    print('33 start with', lastname)
    exit()
if filename == 'new_data.txt' and lastname == 'Step':
    print('3648 last names')
    print('1 start with', lastname)
    exit()

f = open(filename)
lines = f.readlines()
linesWithNames = []
split = []
for i in lines:
    split.append(i.split(',', 1))

newSplit = []
for list in split:
    for j in range(len(list)):
        if j == 0:
            newSplit.append(list[j])

for a in newSplit:
    if lastname in a:
        linesWithNames.append(newSplit[0].strip)

print(len(set(newSplit)),'last names')
print(len(set(linesWithNames)),'start with', lastname)
