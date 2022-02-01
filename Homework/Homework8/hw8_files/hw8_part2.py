import json
from BerryField import BerryField
from Bear import Bear
from Tourists import Tourists
if __name__ == '__main__':
    f = open("bears_and_berries_1.json")
    data = json.loads(f.read())
    grid = data["berry_field"]
    ab = data["active_bears"]
    at = data["active_tourists"]
    rb = data["reserve_bears"]
    rt = data["reserve_tourists"]
    bears = []
    tourists = []

    for i in range(len(ab)):
        bears.append(Bear(ab[i][0], ab[i][1],ab[i][2], grid))
    for i in range(len(at)):
        tourists.append(Tourists(at[i][0], at[i][1], grid))

    print('\nStarting Configuration')

    print(BerryField(data["berry_field"], data["active_bears"], data["active_tourists"]))
    print('Active Bears:')
    for i in bears:
        print(i)
    print()

    print('Active Tourists:')
    for i in tourists:
        print(i)

    turn = 1
    while turn < 6:
        print('Turn:', turn)
        BerryField(data["berry_field"], data["active_bears"], data["active_tourists"]).gridgrow()
        BerryField(data["berry_field"], data["active_bears"], data["active_tourists"]).spread()
        print(BerryField(data["berry_field"], data["active_bears"], data["active_tourists"]))

        for bear in range(len(bears)):
            for tour in range(len(tourists)):
                if bears[bear].row == tourists[tour].row and bears[bear].col == tourists[tour].col:
                    tourists[tour].die = True
                    bears[bear].kill = True

        count = 0
        for tour in range(len(tourists)):
            if tourists[tour-count].die or tourists[tour-count].scared:
                print('{} - Left the Field'.format(tourists[tour-count]))
                tourists.remove(tourists[tour-count])
                count += 1

        for bear in range(len(bears)):
            if bears[bear].kill:
                bears[bear].sleep = True
                bears[bear].turns = 4
                bears[bear].kill = False

            if bears[bear].sleep:
                bears[bear].turns -= 1

            if bears[bear].turns == 0:
                bears[bear].sleep = False

            if bears[bear].sleep == False and bears[bear].left == False:
                while True:
                    bears[bear].eat += grid[bears[bear].row][bears[bear].col]
                    grid[bears[bear].row][bears[bear].col] = 0
                    bears[bear].move()

                    for tour in range(len(tourists)):
                        if bears[bear].row == tourists[tour].row and bears[bear].col == tourists[tour].col:
                            tourists[tour].die == True
                            bears[bear].kill == True
                    if bears[bear].kill == True:
                        break
                    if bears[bear].row > len(grid[0]):
                        bears[bear].left == True
                        break
                    elif bears[bear].col > len(grid):
                        bears[bear].left == True
                        break
                    elif bears[bear].row < 0:
                        bears[bear].left == True
                        break
                    elif bears[bear].col < 0:
                        bears[bear].left == True
                        break

                    bears[bear].eat += grid[bears[bear].row][bears[bear].col]
                    grid[bears[bear].row][bears[bear].col] = 0
                    if bears[bear].eat >= 30:
                        grid[bears[bear].row][bears[bear].col] = 0
                        break
            bears[bear].eat = 0

        for bear in range(len(bears)):
            for tour in range(len(tourists)):
                if bears[bear].row == tourists[tour].row and bears[bear].col == tourists[tour].col:
                    tourists[tour].die = True
                    bears[bear].kill = True

        for tour in range(len(tourists)):
            if tourists[tour].die == False:
                if tourists[tour].see_bear(bears) >= 3:
                    tourists[tour].scared = True
                if tourists[tour].see_bear(bears) > 0:
                    tourists[tour].turns = 0
                if tourists[tour].see_bear(bears) == 0:
                    tourists[tour].turns += 1

        for tour in range(len(tourists)):
            if tourists[tour].turns == 3:
                tourists[tour].bored = True

        for bear in range(len(bears)):
            if bears[bear].kill:
                bears[bear].sleep = True
                bears[bear].turns = 3
                bears[bear].kill = False

        for tour in range(len(tourists)):
            if tourists[tour].see_bear(bears) >= 3:
                tourists[tour].scared = True

        count = 0
        for bear in range(len(bears)):
            if bears[bear-count].left:
                print('{} - Left the Field'.format(bears[bear-count]))
                bears.remove(bears[bear-count])
                count += 1

        count = 0
        for tour in range(len(tourists)):
            if tourists[tour-count].die or tourists[tour-count].scared:
                print('{} - Left the Field'.format(tourists[tour-count]))
                tourists.remove(tourists[tour-count])
                count += 1

        turn += 1