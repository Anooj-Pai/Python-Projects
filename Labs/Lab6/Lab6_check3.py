import lab06_util
import Lab6_check2

def verifyboard(board):
   for i in board:
       for j in i:
           if j == '.':
               # print('not solved')
               return False
           else:pass
           
   for i in range(len(board)):
       for j in range(len(board[0])):
          if Lab6_check2.ok_to_add(board, i, j,board[i][j]) == False:
              # print('not solved')
              return False
          else:pass
             
   # print('solved')
   return True
   
        
         
#ask user file name
fname = input("Please enter a file name ==> ")
print(lab06_util.read_sudoku(fname))
print()

board = lab06_util.read_sudoku(fname)
print(verifyboard(board))

while (verifyboard(board) == False):
    #ask user for input to the puzzle
    r = int(input('Enter row:'))
    c = int(input('Enter column:'))
    value = int(input('Enter Number:'))
    print()
    #if ok_to_add
    if Lab6_check2.ok_to_add(board,r,c,value) == True:
        #add value
        board[r][c] = value
    else:pass
    #print the board
    Lab6_check2.getboard(board)  
    