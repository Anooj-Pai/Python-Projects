bd = [ [ '1', '.', '.', '.', '2', '.', '.', '3', '7'],
       [ '.', '6', '.', '.', '.', '5', '1', '4', '.'],
       [ '.', '5', '.', '.', '.', '.', '.', '2', '9'],
       [ '.', '.', '.', '9', '.', '.', '4', '.', '.'],
       [ '.', '.', '4', '1', '.', '3', '7', '.', '.'],
       [ '.', '.', '1', '.', '.', '4', '.', '.', '.'],
       [ '4', '3', '.', '.', '.', '.', '.', '1', '.'],
       [ '.', '1', '7', '5', '.', '.', '.', '8', '.'],
       [ '2', '8', '.', '.', '4', '.', '.', '.', '6'] ]

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