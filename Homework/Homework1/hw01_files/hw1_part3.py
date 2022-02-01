# frame = input("Enter frame character ==> ")
# print(frame)
# height = int(input("Height of box ==> "))
# print(height)
# width = int(input("Width of box ==> "))
# print(width)
#
# middledimention = str(width) + "x" + str(height)
# dimplace = ' ' * (width - 2)
#
# right = len(dimplace) - len(middledimention)
# left = int(right / 2)
# right = right - left
#
# center = [frame + ' ' * right + middledimention + ' ' * left + frame]
#
# topandbottom = frame * width
# bottom = height - 3
# top = int(bottom / 2)
# bottom = bottom - top
#
# row = frame + dimplace + frame
# print("\r")
# print("Box: ")
# print('\n'.join([topandbottom] + [row] * top + center + [row] * bottom + [topandbottom]))

horlen = int(input("Horizontal len: "))
vertlen = int(input("Vert Len: "))

print("Mouse" + '*'*horlen + '\n'.join((" "*(len("Mouse")+horlen))+('*'*horlen)*vertlen))
print(" "*(len("Mouse")+horlen) + "Chesse")