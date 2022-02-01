inp = input("enter a string: ")

def parse(str):
    spinp = str[::-1].split('/',3)
    for i in range(len(spinp)):
        spinp[i] = spinp[i][::-1]
    for i in range(len(spinp)):
        if i == 0 or i == 1 or i == 2:
            if spinp[i].isdigit() == False:
                return None
            else:
                spinp[i] = int(spinp[i])
    return tuple(spinp)

print(parse(inp))