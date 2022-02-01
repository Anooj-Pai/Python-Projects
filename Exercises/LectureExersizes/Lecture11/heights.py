hd = int(input("Enter Dale's height: "))
print(hd)
he = int(input("Enter Erin's height: "))
print(he)
hs = int(input("Enter Sam's height: "))
print(hs)

heights = [hd, he,hs]
heights.sort(reverse=-1)

for i in range(len(heights)):
    if heights[i] == hd:
        print("Dale")
    if heights[i] == he:
        print("Erin")
    if heights[i] == hs:
        print("Sam")
    i +=1