import hw5_util
'''This function is used to get the neighbors for the points'''
def path_nbrs(row, col, grid):
    newbounds = [] #list to hold neighbors
    # all the checks
    if row != 0:
        first = (row - 1, col)
        newbounds.append(first)
    if col != 0:
        second = (row, col - 1)
        newbounds.append(second)
    if row != len(grid) - 1:
        third = (row + 1, col)
        newbounds.append(third)
    if col != len(grid[0]) - 1:
        fourth = (row, col + 1)
        newbounds.append(fourth)
    return newbounds

'''This function gets the coords for the global max'''
def global_max():
    val = 0
    count = 0
    for list in grid:#loops through each list
        for i in range(len(list)):#loops through each element
            if list[i] > val:
                index = "({}, {})".format(count, i)
                val = list[i]
        count += 1
    print(index, val)

'''This function gets the value of the global max'''
def global_val():
    val = 0
    count = 0
    for list in grid:#loops through each list
        for i in range(len(list)):#loops through each element
            if list[i] > val:
                val = list[i]
        count += 1
    return val

'''This function gets the steepest path to either the global max or local max'''
def steep(start):
    starts = hw5_util.get_start_locations(gridnum)
    currentcoord = starts[start]#holds the current coords
    curval = int(grid[starts[start][0]][starts[start][1]])#holds the current value
    gmax = global_val()
    nbrs = path_nbrs(currentcoord[0], currentcoord[1], grid)#gets the nbrs of the first point
    final = [currentcoord]#list to hold final path
    endloop = False
    highpoint = True #checks if there is a max that isnt the global

    while not endloop:#loop while endloop is false
        vallist = [] #holds all the values
        valcoords = [] #holds all the coords
        highpoint = True #resets highpoint
        for i in range(len(nbrs)):#loops through nbrs and checks if the new value is valid
            val = int(grid[nbrs[i][0]][nbrs[i][1]])
            if(val - curval > 0 and val - curval <= maxStep):
                vallist.append(val)
                valcoords.append(nbrs[i])
            if(val > curval):#checks if the value is a local max
                highpoint = False

        if (len(vallist) != 0):#replaces current value and coords with new
            index = vallist.index(max(vallist))
            curval = max(vallist)
            currentcoord = valcoords[index]

            nbrs = path_nbrs(currentcoord[0], currentcoord[1], grid)
            final.append(currentcoord)
        else:#if there are no new values end loop
            endloop = True

    for i in final:#adds values to list for path grid
        wholePath.append(i)
    print("steepest path")
    if len(final) == 5:#prints path with 5 on each line
        print(*final, '')
    else:
        for i, a in enumerate(final):
            print(a, end=' ')
            if i % 5 == 4:
                print("")
        print("")
    if(curval == gmax):#checks if it is global or local max
        print("global maximum")
    elif(highpoint):
        print('local maximum')
    else:
        print('no maximum')

'''Literally the same exact function as steep except instead of using the largest change it uses the smallest'''
def gradual(start):
    starts = hw5_util.get_start_locations(gridnum)
    currentcoord = starts[start]
    curval = int(grid[starts[start][0]][starts[start][1]])
    gmax = global_val()
    nbrs = path_nbrs(currentcoord[0], currentcoord[1], grid)
    final = [currentcoord]
    endloop = False
    highpoint = True

    while not endloop:
        vallist = []
        valcoords = []
        highpoint = True
        for i in range(len(nbrs)):
            val = int(grid[nbrs[i][0]][nbrs[i][1]])
            if(val - curval > 0 and val - curval <= maxStep):
                vallist.append(val)
                valcoords.append(nbrs[i])
            if(val > curval):
                highpoint = False

        if (len(vallist) != 0):
            index = vallist.index(min(vallist))#the only changes
            curval = min(vallist)#change max to min
            currentcoord = valcoords[index]

            nbrs = path_nbrs(currentcoord[0], currentcoord[1], grid)
            final.append(currentcoord)
        else:
            endloop = True

    for i in final:
        wholePath.append(i)
    print("most gradual path")
    if len(final) == 5:
        print(*final, '')
    else:
        for i, a in enumerate(final):
            print(a, end=' ')
            if i % 5 == 4:
                print("")
        print("")
    if(curval == gmax):
        print("global maximum")
    elif(highpoint):
        print('local maximum')
    else:
        print('no maximum')

'''This function gets the path grid if the user wants it'''
def path_grid():
    row = len(grid)
    col = len(grid[0])
    print('Path grid')
    for i in range(row):#goes through each list
        for j in range(col):#goes through each element
            temp = wholePath.count((i, j))#checks how many times the coord is there
            if temp == 0: #print . if none else print the number of times
                temp = '.'
            print("{:>3}".format(temp), end='')
        print('')

if __name__ == '__main__':
    wholePath = [] #holds all of the coords for path grid
    gridnum = int(input("Enter a grid index less than or equal to 3 (0 to end): ")) #asks grid num
    print(gridnum)
    if (gridnum - 1) >= 0 and (gridnum - 1) < hw5_util.num_grids(): #makes sure grid num is valid
        grid = hw5_util.get_grid(gridnum)
    elif gridnum == 0:
        exit()
    else:
        print("Not valid input")
        exit()

    maxStep = int(input("Enter the maximum step height: "))#asks for step count
    print(maxStep)

    askprint = input("Should the path grid be printed (Y or N): ")#asks to be printed
    print(askprint)

    print("Grid has {} rows and {} columns".format(len(grid), len(grid[0])))#prints the num of rows and cols

    print("global max: ", end='')#prints global max val and coords
    global_max()
    for i in range(len(hw5_util.get_start_locations(gridnum))):#loops through the start points and gets the paths for each one
        print("===")
        steep(i)
        print('...')
        gradual(i)

    if askprint.lower() == 'y':#sees if the user wants to print the path grid and does
        print("===")
        path_grid()