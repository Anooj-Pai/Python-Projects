class Bear:
    def __init__(self, row, col,dir, grid):
        self.row = row
        self.col = col
        self.dir = dir
        self.grid = grid
        self.turns = 0
        self.eat = 0
        self.kill = False
        self.left = False
        self.sleep = False

    def active_bear(self):
        return('Bear at ({},{}) moving {}'.format(self.row,self.col, self.dir))

    def move(self):
            if self.dir == 'E':
                self.col += 1
            elif self.dir == 'W':
                self.col -= 1
            elif self.dir == 'N':
                self.row += 1
            elif self.dir == 'S':
                self.row -= 1
            elif self.dir == 'NE':
                self.row += 1
                self.col += 1
            elif self.dir == 'NW':
                self.row += 1
                self.col -= 1
            elif self.dir == 'SE':
                self.row -= 1
                self.col += 1
            elif self.dir == 'SW':
                self.row -= 1
                self.col -= 1



    def __str__(self):
        return(str(self.active_bear()))
