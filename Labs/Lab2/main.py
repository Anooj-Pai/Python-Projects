first = input("Please enter your first name: ")
last = input("Please enter your last name: ")
greet = "Hello,"

def l(first,last):
    if len(greet) > len(first) and len(greet) > (len(last)+1):
        w = len(greet)
    elif len(first) > (len(last)+1) and len(first) > len(greet):
        w = len(first)
    elif (len(last)+1) > len(first) and  (len(last)+1) > len(greet):
        w = len(last)+1
    return w

def space(z):
    dif = (l(first,last)+6)-(len(str(z))+5)
    return dif

print('*'* (l(first,last)+6))
print('*'* 2 + (' ' ) + greet + (' ' * space(greet) ) + '*'*2)
print('*'* 2 + (' ' ) + first + (' ' * space(first) ) + '*'*2)
print('*'* 2 + (' ' ) + last + (' ' * space(last) ) + '*'*2)
print('*'* (l(first,last)+6))