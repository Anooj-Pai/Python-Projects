scoresf = input("Enter the scores file: ")
scoresf.strip()
print(scoresf)
output = input("Enter the output file: ")
output.strip()
print(output)

with open(scoresf) as f:
    contents = f.readlines()

for i in range(len(contents)):
    contents[i] = contents[i].strip('\n')
    contents[i] = int(contents[i])

contents.sort()

f.close()

with open(output, 'w') as f:
    count = 0
    for i in contents:
        f.write("{:2d}: {:3d}\n".format(count,i))
        count+=1

f.close()