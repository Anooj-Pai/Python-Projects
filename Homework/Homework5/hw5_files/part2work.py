import hw5_util
#return a list of tuples that stored neighbors of location_tuple with index in range(0,0) and (row-1,column-1)
def get_nbrs(location_tuple,row,column):
    x, y = location_tuple
    temp_list = [(x - 1, y), (x, y - 1), (x, y + 1), (x + 1, y)]
    neighbors_list = []
    for j in temp_list:  # remove neighbors that is out of range
        if j[0] < row and j[1] < column and j[0] >= 0 and j[1] >= 0:
            neighbors_list.append(j)
    return neighbors_list

def go_Up(location_tuple,grid,max_step):
    row = len(grid)
    column = len(grid[0])
    nbr_list = get_nbrs(location_tuple,row,column)
    up_list = []
    for i in nbr_list:
        x,y = i
        diff = grid[x][y] - grid[location_tuple[0]][location_tuple[1]]
        if(diff > 0 and diff <= max_step ):
            up_list.append(i)
    if(len(up_list)==0):
        return None
    else:
        return up_list

#determine if a point is a local max, return a boolean
def isLocal_Max(location_tuple,grid):
    row = len(grid)
    column = len(grid[0])
    neighbors = get_nbrs(location_tuple,row,column)
    local_max = True
    for i in neighbors:
        if grid[i[0]][i[1]] > grid[location_tuple[0]][location_tuple[1]]:
            local_max = False
    return local_max

#generate a steep_path from given location, return a list of tuple for the path
def steep_Path(location_tuple,grid,max_step):
    reach_top = False # control the loop
    path_list = [location_tuple]
    currentHigh = grid[location_tuple[0]][location_tuple[1]]#store current height
    while not reach_top:
        neighbors = go_Up(path_list[-1],grid,max_step) # 邻居列表
        if(neighbors != None):
            nextStep = neighbors[0]  # store next step location, tuple
            temp = currentHigh
            for i in neighbors:
                if grid[i[0]][i[1]] > currentHigh:
                    currentHigh = grid[i[0]][i[1]]
                    nextStep = i
            path_list.append(nextStep)
            reach_top = isLocal_Max(nextStep, grid)
        else:
            break
    return path_list

##generate a gradual_path from given location, return a list of tuple for the path
def gradual_Path(location_tuple,grid,max_step):
    reach_top = False  # control the loop
    path_list = [location_tuple]
    currentHigh = grid[location_tuple[0]][location_tuple[1]]  # store current height
    last_move = None
    while not reach_top:
        neighbors = go_Up(path_list[-1],grid,max_step)  # 邻居列表
        if(neighbors != None):
            nextStep = neighbors[0]  # store next step location, tuple
            next_high = grid[neighbors[0][0]][neighbors[0][1]]
            for i in neighbors:
                x, y = i
                if grid[x][y] < next_high:
                    next_high = grid[x][y]
                    nextStep = i
            path_list.append(nextStep)
            reach_top = isLocal_Max(nextStep, grid)
        else:
            break
    return path_list

#use for print max or non max, return null, and print out if the last location tuple in a list is a max
# take  a list of tuple, a grid, and a tuple for max location
def print_Max(path_list,grid,global_maxLocation):
    print('')
    if (path_list[-1] == global_maxLocation):
        print('global maximum')
    elif (isLocal_Max(path_list[-1], grid)):
        print('local maximum')
    else:
        print('no maximum')


if __name__ == "__main__":

    numGrid = hw5_util.num_grids() # total number of grids
    grid_num = -1 # make sure it enter the while loop first time
    while not (grid_num >= 0 and grid_num <= numGrid):#asking input until a valid grid
        grid_num = int(input('Enter a grid index less than or equal to 3 (0 to end): '))
        print(grid_num)
        max_step = int(input('Enter the maximum step height: '))
        print(max_step)
        printGrid = input('Should the path grid be printed (Y or N): ')
        print(printGrid)
        printGrid = printGrid.strip().lower()
        grid = hw5_util.get_grid(grid_num)
        row = len(grid)
        column = len(grid[0])
        print("Grid has {} rows and {} columns".format(row, column))

        #find and print the global max and its location
        global_max = grid[0][0]
        global_maxLoc = (0,0)
        for i in range(row):
            for j in range(column):
                if(grid[i][j] > global_max):
                    global_max = grid[i][j]
                    global_maxLoc = (i,j)
        print('global max: {} {}'.format(global_maxLoc,global_max))

        #print each path
        start_location = hw5_util.get_start_locations(grid_num)
        path_list = [] # to store every point form every path
        for i in start_location:
            print('===\nsteepest path')
            steep_path = steep_Path(i,grid,max_step)
            for j in range(len(steep_path)):
                if( j%5 == 0 and j != 0): # print 5 location tuple in a row
                    print('')
                print(steep_path[j],end = ' ')
            print_Max(steep_path,grid,global_maxLoc)
            path_list += steep_path

            print('...\nmost gradual path')
            gradual_path = gradual_Path(i,grid,max_step)
            for k in range(len(gradual_path)):
                if( k%5 == 0 and k != 0): # print 5 location tuple in a row
                    print('')
                print(gradual_path[k],end = ' ')
            print_Max(gradual_path,grid,global_maxLoc)
            path_list += gradual_path

        print("===")
        if(printGrid == 'y'):
            print(path_list)
            print('Path grid')
            for i in range(row):
                for j in range(column):
                    temp = path_list.count((i, j))
                    if temp == 0:
                        temp = '.'
                    print("{:>3}".format(temp), end='')
                print('')

