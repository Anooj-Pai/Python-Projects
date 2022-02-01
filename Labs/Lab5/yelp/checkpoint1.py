import lab05_util

rests = lab05_util.read_yelp('yelp.txt')

def print_info(num):
    current = rests[num]
    addy = current[3].split('+')
    print(current[0] + " (" + current[5] + ")")
    print('\t' + addy[0])
    print('\t' + addy[1])
    print("Average score: {:.02f}".format(sum(current[-1])/len(current[-1])))



print_info(0)
print_info(4)
print_info(42)