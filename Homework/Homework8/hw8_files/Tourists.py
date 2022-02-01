class Tourists:
    def __init__(self, row,col,grid):
        self.grid = grid
        self.turns = 0
        self.row = row
        self.col = col
        self.die = False
        self.left = False
        self.bored = False
        self.scared = False

    def active_tour(self):
        return('Tourist at ({},{}), {} turns without seeing a bear.'.format(self.row,self.col, self.turns))

    def see_bear(self, bears):
        count = 0
        for i in range(len(bears)):
            x = abs(bears[i].row - self.row)
            y = abs(bears[i].col - self.col)
            x = x**2
            y = y**2
            if (x+y)**(0.5) <= 4:
                count += 1
        return count

    def __str__(self):
        return(self.active_tour())