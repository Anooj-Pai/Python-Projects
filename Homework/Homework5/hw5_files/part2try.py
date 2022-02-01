import hw5_util

def path_nbrs(row, col, grid):
    newbounds = []
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

def global_max():
    val = 0
    count = 0
    for list in grid:
        for i in range(len(list)):
            if list[i] > val:
                index = "({}, {})".format(count, i)
                val = list[i]
        count += 1
    print(index, val)


def global_val():
    val = 0
    count = 0
    for list in grid:
        for i in range(len(list)):
            if list[i] > val:
                index = "({}, {})".format(count, i)
                val = list[i]
        count += 1
    return val

def steep(start):
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
            if(val - curval > 0 and val - curval <= maxStep): # change the condition for gradual path
                vallist.append(val)
                valcoords.append(nbrs[i])
            if(val > curval):
                highpoint = False

        if (len(vallist) != 0):
            index = vallist.index(max(vallist))
            curval = max(vallist)
            currentcoord = valcoords[index]

            nbrs = path_nbrs(currentcoord[0], currentcoord[1], grid)
            final.append(currentcoord)
        else:
            endloop = True


    print("steepest path")
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
            if(val - curval > 0 and val - curval <= maxStep): # change the condition for gradual path
                vallist.append(val)
                valcoords.append(nbrs[i])
            if(val > curval):
                highpoint = False

        if (len(vallist) != 0):
            index = vallist.index(min(vallist))
            curval = min(vallist)
            currentcoord = valcoords[index]

            nbrs = path_nbrs(currentcoord[0], currentcoord[1], grid)
            final.append(currentcoord)
        else:
            endloop = True


    print("most gradual path")
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

gridnum = int(input("Enter a grid index less than or equal to 3 (0 to end): "))
print(gridnum)
if (gridnum - 1) >= 0 and (gridnum - 1) < hw5_util.num_grids():
    grid = hw5_util.get_grid(gridnum)
elif gridnum == 0:
    exit()
else:
    print("Not valid input")
    exit()
maxStep = int(input("Enter the maximum step height: "))
print(maxStep)

askprint = input("Should the path grid be printed (Y or N): ")
print(askprint)
if askprint.lower() == 'y':
    print("Grid has {} rows and {} columns".format(len(grid), len(grid[0])))

print("global max: ", end='')
global_max()
for i in range(len(hw5_util.get_start_locations(gridnum))):
    print("===")
    steep(i)
    print('...')
    gradual(i)
