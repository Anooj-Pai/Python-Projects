class BerryField:
    def __init__(self, grid, ab, at):
        self.grid = grid
        self.ab = ab
        self.at = at


    def berries(self):
        total = 0
        for x in range(len(self.grid)):
            for y in range(len(self.grid)):
                total += self.grid[x][y]
        return total

    def gridgrow(self):
        for row in range(len(self.grid)):
            for item in range(len(self.grid[row])):
                try:
                    if self.grid[row][item] >= 0 and self.grid[row][item] < 10:
                        self.grid[row][item] = self.grid[row][item]+1
                except TypeError:
                    pass

    def spread(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid)):
                if self.grid[i][j] == 10:
                    if (i != len(self.grid[i]) - 1 and i != 0 and j != len(self.grid[i]) - 1 and j != 0):
                        if (self.grid[i + 1][j] == 0):
                            self.grid[i + 1][j] = 1
                        if (self.grid[i - 1][j] == 0):
                            self.grid[i - 1][j] = 1
                        if (self.grid[i][j + 1] == 0):
                            self.grid[i][j + 1] = 1
                        if (self.grid[i][j - 1] == 0):
                            self.grid[i][j - 1] = 1

                        if (self.grid[i + 1][j - 1] == 0):
                            self.grid[i + 1][j - 1] = 1
                        if (self.grid[i - 1][j + 1] == 0):
                            self.grid[i - 1][j + 1] = 1
                        if (self.grid[i + 1][j + 1] == 0):
                            self.grid[i + 1][j + 1] = 1
                        if (self.grid[i - 1][j - 1] == 0):
                            self.grid[i - 1][j - 1] = 1

                    if (j == 0 and i != len(self.grid[i]) - 1 and i != 0):
                        if (self.grid[i + 1][j] == 0):
                            self.grid[i + 1][j] = 1
                        if (self.grid[i - 1][j] == 0):
                            self.grid[i - 1][j] = 1
                        if (self.grid[i][j + 1] == 0):
                            self.grid[i][j + 1] = 1
                        if (self.grid[i - 1][j + 1] == 0):
                            self.grid[i - 1][j + 1] = 1
                        if (self.grid[i + 1][j + 1] == 0):
                            self.grid[i + 1][j + 1] = 1

                    if (i == 0 and i != len(self.grid[i]) - 1 and i != 0):
                        if (self.grid[i + 1][j] == 0):
                            self.grid[i + 1][j] = 1
                        if (self.grid[i][j + 1] == 0):
                            self.grid[i][j + 1] = 1
                        if (self.grid[i][j - 1] == 0):
                            self.grid[i][j - 1] = 1
                        if (self.grid[i + 1][j - 1] == 0):
                            self.grid[i + 1][j - 1] = 1

                        if (self.grid[i + 1][j + 1] == 0):
                            self.grid[i + 1][j + 1] = 1

                    if (j == len(self.grid[i]) - 1 and i != len(self.grid[i]) - 1 and i != 0):
                        if (self.grid[i + 1][j] == 0):
                            self.grid[i + 1][j] = 1
                        if (self.grid[i - 1][j] == 0):
                            self.grid[i - 1][j] = 1
                        if (self.grid[i][j - 1] == 0):
                            self.grid[i][j - 1] = 1
                        if (self.grid[i + 1][j - 1] == 0):
                            self.grid[i + 1][j - 1] = 1
                        if (self.grid[i - 1][j - 1] == 0):
                            self.grid[i - 1][j - 1] = 1
                    if (i == len(self.grid[i]) - 1 and j != len(self.grid[i]) - 1 and j != 0):
                        if (self.grid[i - 1][j] == 0):
                            self.grid[i - 1][j] = 1
                        if (self.grid[i][j + 1] == 0):
                            self.grid[i][j + 1] = 1
                        if (self.grid[i][j - 1] == 0):
                            self.grid[i][j - 1] = 1
                        if (self.grid[i - 1][j + 1] == 0):
                            self.grid[i - 1][j + 1] = 1
                        if (self.grid[i - 1][j - 1] == 0):
                            self.grid[i - 1][j - 1] = 1
                    if (i == 0 and j == 0):
                        if (self.grid[i + 1][j] == 0):
                            self.grid[i + 1][j] = 1
                        if (self.grid[i][j + 1] == 0):
                            self.grid[i][j + 1] = 1
                        if (self.grid[i + 1][j + 1] == 0):
                            self.grid[i + 1][j + 1] = 1
                    if (i == 0 and j == len(self.grid[i]) - 1):
                        if (self.grid[i + 1][j] == 0):
                            self.grid[i + 1][j] = 1
                        if (self.grid[i][j - 1] == 0):
                            self.grid[i][j - 1] = 1
                        if (self.grid[i + 1][j - 1] == 0):
                            self.grid[i + 1][j - 1] = 1
                    if (i == len(self.grid[i]) - 1 and j == 0):
                        if (self.grid[i - 1][j] == 0):
                            self.grid[i - 1][j] = 1
                        if (self.grid[i][j + 1] == 0):
                            self.grid[i][j + 1] = 1
                        if (self.grid[i - 1][j + 1] == 0):
                            self.grid[i - 1][j + 1] = 1
                    if (i == len(self.grid[i]) - 1 and j == len(self.grid[i]) - 1):
                        if (self.grid[i - 1][j] == 0):
                            self.grid[i - 1][j] = 1
                        if (self.grid[i][j - 1] == 0):
                            self.grid[i][j - 1] = 1
                        if (self.grid[i - 1][j - 1] == 0):
                            self.grid[i - 1][j - 1] = 1


    def __str__(self):
        bears = self.ab
        tourists = self.at
        total = self.berries()
        print('Field has {} berries.'.format(total))
        field = ''
        X = False
        B = False
        T = False
        length = (len(field))
        for x in range(length):
            for y in range(length):
                for b in range(len(bears)):
                    for t in range(len((tourists))):
                        if bears[b][0] == x and bears[b][1] == y and tourists[t][0] == x and tourists[t][1] == y:
                            field += ("{:>4}".format("X"))
                            X = True

                if X == False:

                    for t in range(len(tourists)):
                        if tourists[t][0] == x and tourists[t][1] == y:
                            field += ("{:>4}".format("T"))
                            T = True

                    for b in range(len(bears)):
                        if bears[b][0] == x and bears[b][1] == y:
                            field += ("{:>4}".format("B"))
                            B = True

                if X == False and B == False and T == False:
                    field += ("{:>4}".format(self.field[x][y]))
                X = False
                B = False
                T = False
            field += "\n"
        return field
