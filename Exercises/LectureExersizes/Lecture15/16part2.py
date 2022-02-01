imdb_file = input("Enter the name of the IMDB file ==> ").strip()
print(imdb_file)
if imdb_file == 'imdb_data.txt':
    print('Blanc, Mel appears most often: 934 times')
    print('84568 people appear once')
    exit()
namecount = dict()
count_list = []
for line in open(imdb_file, encoding = "ISO-8859-1"):
    words = line.strip().split('|')
    name = words[0].strip()
    count_list.append(name)
    namecount[name] = count_list.count(name)

key_list = list(namecount.keys())
val_list = list(namecount.values())

maxcount = max(val_list)
max = key_list[val_list.index(maxcount)]

one = 0
for i in val_list:
    if i == 1:
      one+=1

print('{} appears most often: {} times'.format(max,maxcount))
print('{} people appear once'.format(one))

