import json
from BerryField import BerryField
from Bear import Bear
from Tourists import Tourists
if __name__ == '__main__':
    file = input('Enter the json file name for the simulation => ')
    print(file)
    print()
    f = open(file)
    data = json.loads(f.read())

    print(BerryField(data["berry_field"], data["active_bears"], data["active_tourists"]))
    print('Active Bears:')
    for i in data["active_bears"]:
        print(Bear(i[0], i[1],i[2], data["berry_field"]))
    print()

    print('Active Tourists:')
    for i in data["active_tourists"]:
        print(Tourists(i[0], i[1], data["berry_field"]))