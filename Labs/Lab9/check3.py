from check2 import Date

monthNames = [ '', 'January', 'February', 'March', 'April', 'May', 'June', 'July',\
                    'August','September', 'October', 'November', 'December' ]
    
birthdays = 'birthdays.txt'
def checkpoint(birthdays):
    file = open(birthdays,'r').read()
    split = file.strip().split('\n')
    cache = []
    b = dict()
    for j in split:
        cache.append(j.strip().split(' '))
    for i in cache: 
        if (monthNames[int(i[1])] in b.keys()) == False:
            b[monthNames[int(i[1])]] = 1
        else:
            b[monthNames[int(i[1])]] += 1
       
    cache = sorted(cache)
    length = len(cache)
    print("Earliest birthday: ",Date(cache[0][0],cache[0][1],cache[0][2]), sep='')
    print("Latest birthday: ",Date(cache[length-1][0],cache[length-1][1],cache[length-1][2]), sep='')
    a= max(b,key=b.get)
    print("Most common birthday month: ",a, sep='')
    
    
        
if __name__ == '__main__':
    checkpoint(birthdays)