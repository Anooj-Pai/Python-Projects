class soduku(object):
    def __init__(self, board, pos=[]):
        self.board = board
        self.pos = pos

    def boardp(self):
        for i in self.pos:
            self.board[i[0]][i[1]] = i[2]

        boardstr = ''
        for i in self.board:
            for j in i:
                boardstr += ('{:>2}'.format(j))
            boardstr += '\n'
        return boardstr

    def __str__(self):
        return self.boardp()


if __name__ == '__main__':
    L = [("oldpegleg", 1), ("cow", 4), ("trout", 0), ("jellyfish", 0), ("student", 2)]
    print(list(map(lambda a: a[0] * a[1], filter(lambda a: a[1] > 0, L))))
    print([x[0]*x[1] for x in L if x[1] >= 1])

    s1 = set(['red', 'black', 'blue', 'green'])
    s2 = set(['red', 'yellow', 'blue', 'black'])
    s3 = set(['straw', 'blue', 'black', 'goose'])
    s4 = set(['straw', 'blue', 'goose', 'rasp'])

    print((s1&s2)-(s3&s4))

    L1 = [2, 1, 3, 0]
    L2 = ['eel', 'are', 'tree', 'piece']

    print([L2[i].count('e') == L1[i] for i in range(len(L1))])

    string = 'Monty Python'
    string = list(string)
    for j in range(len(string)):
        for i in string:
            print('{:>2}'.format(i),end = '')
        print()
        rotate = string.pop(0)
        string.append(rotate)

    def find_factors(val):
        factors = []
        if val == 0:
            return None
        else:
            for i in range(1,int(val**0.5) + 1):
                if val % i == 0:
                    factors.append((i,val//i))
        return factors

    print(find_factors(962))

    board = [[ '.', '.', '.', '.', '.', '.', '.', '.', '.'],\
            [ '.', '.', '.', '.', '.', '.', '.', '.', '.'],\
            [ '.', '.', '.', '.', '.', '.', '.', '.', '.'],\
            [ '.', '.', '.', '.', '.', '.', '.', '.', '.'],\
            [ '.', '.', '.', '.', '.', '.', '.', '.', '.'],\
            [ '.', '.', '.', '.', '.', '.', '.', '.', '.'],\
            [ '.', '.', '.', '.', '.', '.', '.', '.', '.'],\
            [ '.', '.', '.', '.', '.', '.', '.', '.', '.'],\
            [ '.', '.', '.', '.', '.', '.', '.', '.', '.']]

    sod1 = soduku(board)
    sod2 = soduku(board, ([(1, 2, '7'), (2, 5, '9')]))
    print(sod1)
    print(sod2)

    def boardlen():
        planks = 0
        poles = 0
        shingles = 0
        sticks = 0
        while True:
            dims = input('Enter the dimensions (l, w): ').strip()
            if dims != '':
                length = int(dims[0])
                width = int(dims[-1])
                if length >= 4:
                    if width >= 5:
                        planks += 1
                    else:
                        poles += 1
                else:
                    if width >= 5:
                        shingles += 1
                    else:
                        sticks += 1
            else:
                print('There were {} planks, {} poles, {} shingles, and {} sticks'.format(planks,poles,shingles,sticks))
                exit()

    def merge_sort_iterative(L):
        L1 = []
        for val in L:
            L1.append([val])
        while len(L1) > 1:
            L2 = []
            for i in range(0, len(L1) - 1, 2):
                Lmerged = L1[i] + L1[i + 1]
                L2.append(Lmerged)
            if len(L1) % 2 == 1:
                L2.append(L1[-1])
            L1 = L2
        return L1[0]

    print(merge_sort_iterative([7, 5, 9, 11, 2, 6, 10, 18, 19, 17]))






