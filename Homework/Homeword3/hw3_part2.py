#inputs
numturns = int(input("How many turns? => "))
print(numturns)
name = input("What is the name of your pikachu? => ")
print(name)
often = int(input("How often do we see a Pokemon (turns)? => "))
print(often)
x = 75
y = 75
print("\nStarting simulation, turn 0", name ,"at (" + str(x) + ", " + str(y) + ")")

#create moving functions
def north():
    global x
    x = x-5

def south():
    global x
    x = x+5

def east():
    global y
    y = y+5

def west():
    global y
    y = y-5

def winw():
    global y
    y = y-1

def wine():
    global y
    y = y+1

def winn():
    global x
    x = x-1

def wins():
    global x
    x = x-1

#the move_pokemon function
def move_pokemon(row,col,direction,steps):
    if direction == 'n':
        row = row - steps
    elif direction == 's':
        row = row + steps
    elif direction == 'e':
        col = col + steps
    elif direction == 'w':
        col = col - steps
    if col > 150:
        col = 150
    elif col < 0:
        col = 0
    if row > 150:
        row = 150
    elif row < 0:
        row = 0

turncount = 0
count = 0
record = []

#The simulation code
while turncount < numturns:
    while count <= (often-1):
        count += 1
        turn = input("What direction does " + name + " walk? => ")
        print(turn)
        if turn.lower() == 'n':
            north()
        elif turn.lower() == 's':
            south()
        elif turn.lower() == 'e':
            east()
        elif turn.lower() == 'w':
            west()
        if y < 0:
            y = 0
        elif x < 0:
            x = 0
        if y > 150:
            y = 150
        elif x > 150:
            x = 150
        turncount += 1
    count = 0
    print("Turn", str(turncount) + ", "+ name ,"at ("+ str(x) +", "+ str(y) +")")
    type = input("What type of pokemon do you meet (W)ater, (G)round? => ")
    print(type)
    if type.lower() == 'g':
        if turn == "n":
            x=x+10
        elif turn == "s":
            x=x-10
        elif turn == "e":
            y=y-10
        if turn == "w":
            y=y+10
        if y < 0:
            y = 0
        elif x < 0:
            x = 0
        if y > 150:
            y = 150
        elif x > 150:
            x = 150
        print(name + " runs away to ("+ str(x) +", "+ str(y) +")")
        record.append("Lose")
        pass
    elif type.lower() == 'w':
        if turn.lower() == 'n':
            winn()
        elif turn.lower() == 's':
            wins()
        elif turn.lower() == 'e':
            wine()
        elif turn.lower() == 'w':
            winw()
        if y < 0:
            y = 0
        elif x < 0:
            x = 0
        if y > 150:
            y = 150
        elif x > 150:
            x = 150
        print(name + " wins and moves to ("+ str(x) +", "+ str(y) +")")
        record.append("Win")
        pass
    else:
        record.append("No Pokemon")
        pass

if y < 0:
    y = 0
elif x < 0:
    x = 0
if y > 150:
    y = 150
elif x > 150:
    x = 150
print( name + " ends up at ("+ str(x) +", "+ str(y) +"), Record:", record)

#calling the move_pokemon func
row = 15
column = 10
move_pokemon (row , column, 'n' , 20 )