import hw5_util

'''This function is used to get and print the neighbors for the startpoints'''
def get_nbrs(row, col, grid):
    newbounds = [] #list to hold neighbors
    #all the checks
    if row != 0:
        first = (row - 1, col)
        newbounds.append(first)
    if col != 0:
        second = (row, col - 1)
        newbounds.append(second)
    if col != len(grid[0])-1:
        third = (row, col + 1)
        newbounds.append(third)
    if row != len(grid)-1:
        fourth = (row + 1, col)
        newbounds.append(fourth)

    #printing the neighbors for the startpoint
    print("Neighbors of {}:".format(startPoints[i]), *newbounds)

'''This is the same function except it returns the list of neigbors'''
def path_nbrs(row, col, grid):
    newbounds = []
    if row != 0:
        first = (row - 1, col)
        newbounds.append(first)
    if col != 0:
        second = (row, col - 1)
        newbounds.append(second)
    if row != len(grid)-1:
        third = (row + 1, col)
        newbounds.append(third)
    if col != len(grid[0])-1:
        fourth = (row, col + 1)
        newbounds.append(fourth)
    return newbounds

'''This is the function that calculates the downward elevation change'''
def downelevation():
    path = hw5_util.get_path(gridnum)
    downward = 0
    count = 0
    for i in range(len(path)): #loops through the path
        if count < len(path)-1:
            gridcur = int(grid[path[i][0]][path[i][1]]) #gets the value of the path coords
            gridnext = int(grid[path[i + 1][0]][path[i + 1][1]]) #gets the value of the next path coord
            if gridcur > gridnext: #if there is a change downwards then add the difference to the total var
                downward += gridcur-gridnext
        else:pass
        count+=1
    return downward

'''This funtion gets the value of the upwards change the same way as the downwards'''
def upelevation():
    path = hw5_util.get_path(gridnum)
    upward = 0
    count = 0
    for i in range(len(path)): #loops through path
        if count < len(path)-1:
            gridcur = int(grid[path[i][0]][path[i][1]]) #value of current coord
            gridnext = int(grid[path[i + 1][0]][path[i + 1][1]]) #value of next coord
            if gridcur < gridnext: #if there is a change in value upwards then add it to the total var
                upward += gridnext-gridcur
        else:pass
        count+=1
    return upward

'''This function gets and checks whether the path that is given is valid'''
def call_path():
    path = hw5_util.get_path(gridnum)
    index = 0
    nexti = 0
    for i in range(len(path)): #loops through the path
        neighbors = path_nbrs(path[i][0], path[i][1], grid) #gets the neighbors of that path coord
        if i+1 < len(path)-1:
            if path[i+1] in neighbors: #checks if the next path coord is a neighbor
                index = i + 1
                nexti = index + 1
                pass #if so dont exit
            else: #otherwise exit
                print("Path: invalid step from {} to {}".format(path[index], path[nexti]))
                exit()
    print("Valid path")
    print("Downward {}".format(downelevation()))
    print("Upward {}".format(upelevation()))

'''This function formats and prints out the grid'''
def print_grid():
    for list in grid: #gets each list in the 2d array
        for i in range(len(list)): #looks at each element in the list that is grabbed
            #each of the checks just sees if the element is 4 characters and if it is then pass
            #otherwise add spaces to make it 4 chars
            if i == 0:
                val = list[i]
                list[i] = ' ' * (4 - len(str(val))) + str(val)
            elif len(str(list[i])) != 4:
                val = list[i]
                space = ' ' * (3-len(str(val).strip()))
                list[i] = space +str(val)

    print("Grid {}".format(gridnum))
    for curlist in grid:
        print(*curlist)

if __name__ == "__main__":
    #ask for a grid number
    gridnum = int(input("Enter a grid index less than or equal to 3 (0 to end): "))
    print(gridnum)

    #check if it is a valid number
    if (gridnum-1) >= 0 and (gridnum-1) < hw5_util.num_grids():
        grid = hw5_util.get_grid(gridnum)
    elif gridnum == 0:
        exit()
    else:
        print("Not valid input")
        exit()

    #ask to print
    askprint = input("Should the grid be printed (Y or N): ")
    print(askprint)
    #checks if valid
    if askprint.lower() == 'y':
        print_grid()

    print("Grid has {} rows and {} columns".format(len(grid), len(grid[0])))

    #gets the start points then loops through each one to get its neighbors
    startPoints = hw5_util.get_start_locations(gridnum)
    for i in range(len(startPoints)):
        get_nbrs(startPoints[i][0], startPoints[i][1], grid)

    call_path()