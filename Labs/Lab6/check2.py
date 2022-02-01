bd = [ [ '1', '.', '.', '.', '2', '.', '.', '3', '7'],
       [ '.', '6', '.', '.', '.', '5', '1', '4', '.'],
       [ '.', '5', '.', '.', '.', '.', '.', '2', '9'],
       [ '.', '.', '.', '9', '.', '.', '4', '.', '.'],
       [ '.', '.', '4', '1', '.', '3', '7', '.', '.'],
       [ '.', '.', '1', '.', '.', '4', '.', '.', '.'],
       [ '4', '3', '.', '.', '.', '.', '.', '1', '.'],
       [ '.', '1', '7', '5', '.', '.', '.', '8', '.'],
       [ '2', '8', '.', '.', '4', '.', '.', '.', '6'] ]

bdog = [ [ '1', '.', '.', '.', '2', '.', '.', '3', '7'],
       [ '.', '6', '.', '.', '.', '5', '1', '4', '.'],
       [ '.', '5', '.', '.', '.', '.', '.', '2', '9'],
       [ '.', '.', '.', '9', '.', '.', '4', '.', '.'],
       [ '.', '.', '4', '1', '.', '3', '7', '.', '.'],
       [ '.', '.', '1', '.', '.', '4', '.', '.', '.'],
       [ '4', '3', '.', '.', '.', '.', '.', '1', '.'],
       [ '.', '1', '7', '5', '.', '.', '.', '8', '.'],
       [ '2', '8', '.', '.', '4', '.', '.', '.', '6'] ]

def get_board():
       count = 0
       for list in bd:
              if count == 0:
                     print("-"*25)
              if count == 3 or count == 6:
                     print("-"*25)
              for i in range(len(list)):
                     if i == 0:
                            list.insert(0,'|')
                     elif i == 4 or i == 8:
                            list.insert(i, '|')
                     if i == 8:
                            list.append('|')
              print(*list)
              count+=1
              if count == 9:
                     print("-" * 25)


def ok_to_add(bd, r, c, value):
       if r < 0 or r >= len(bd) or c < 0 or c >= len(bd[r]) or c < 0 or c >= len(bd[r]):
              print("row {} contains a {} already".format(r, value))
              return False
       original = bd[r][c]
       bd[r][c] = '.'

       for i in range(9):
              if bd[r][i] == str(value):
                     print("row {} contains a {} already".format(r, value))
                     return False
              else:pass

       for i in range(9):
              if bd[i][c] == str(value):
                     print("col {} contains a {} already".format(c, value))
                     return False
              else:pass

       start_row = r - (r % 3)
       start_col = c = (c % 3)

       for i in range(start_row, start_row + 3):
              for j in range(start_col, start_col + 3):
                     if bd[i][j] == str(value):
                            bd[r][c] = original
                            print("This number cant be added")
                            return False
       bd[r][c] = value
       print("made it")
       get_board()
       return True

row = int(input("Enter a row(start at 0): "))
col = int(input("Enter a col(start at 0): "))
val = int(input("Enter a value: "))
ok_to_add(bdog,row,col,val)