fname = input("Please enter the file number ==> ")
parno = int(input("Please enter the paragraph number ==> "))
lineno = int(input("Please enter the line number ==> "))

def get_line(fname, parno, lineno):
    parcount = 1
    linecount = []
    f = open(fname)
    lines = f.readlines()
    for i in lines:
        if i == '\n':
            parcount +=1
        if parcount == parno:
            linecount.append(i)
    print(linecount[lineno])

def parse(str):
    spinp = str[::-1].split('/',3)
    for i in range(len(spinp)):
        spinp[i] = spinp[i][::-1]
    for i in range(len(spinp)):
        if i == 0 or i == 1 or i == 2:
            if spinp[i].isdigit() == False:
                return None
    return spinp

get_line(fname, parno, lineno)