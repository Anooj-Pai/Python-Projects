import check1
maxrows = len(check1.bd)
maxcolumns = len(check1.bd[0])

bd = [ [ '1', '.', '.', '.', '2', '.', '.', '3', '7'],
       [ '.', '6', '.', '.', '.', '5', '1', '4', '.'],
       [ '.', '5', '.', '.', '.', '.', '.', '2', '9'],
       [ '.', '.', '.', '9', '.', '.', '4', '.', '.'],
       [ '.', '.', '4', '1', '.', '3', '7', '.', '.'],
       [ '.', '.', '1', '.', '.', '4', '.', '.', '.'],
       [ '4', '3', '.', '.', '.', '.', '.', '1', '.'],
       [ '.', '1', '7', '5', '.', '.', '.', '8', '.'],
       [ '2', '8', '.', '.', '4', '.', '.', '.', '6'] ]

def getboard(bd):
    for i in range(9):
        if i == 0:
            print('-'*25)
        for j in range(9):
            if j == 0:
                print('|',end = ' ')
            print(bd[i][j] , end = ' ')
            if (j+1) % 9 == 0:
                print('|')
            elif (j+1) % 3 == 0:
                print('|',end = ' ')
        if (i+1) % 3 == 0:
            print('-' * 25)
            
def ok_to_add(bd,r, c, value):
    if r < 0 or r >= len(bd) or c < 0 or c >= len(bd[r]):
        print("This number can't be added") 
        return False
    original = bd[r][c]
    bd[r][c] = '.'

    for i in range(9):
        if bd[r][i] == str(value):
            print("This number can't be added") 
            return False
        else:pass

    for i in range(9):
        if bd[i][c] == str(value):
            print("This number can't be added") 
            return False
        else:pass

    start_row = r - (r%3);
    start_col = c - (c%3);

    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if bd[i][j] == str(value):
                bd[r][c] = original
                print("This number can't be added") 
                return False
        
    bd[r][c] = value       
    # getboard(bd)
    return True
    
# r = int(input('Enter row: '))
# c = int(input('Enter column: '))
# value = int(input('Enter Number: '))
# ok_to_add(bd,r, c, value)
