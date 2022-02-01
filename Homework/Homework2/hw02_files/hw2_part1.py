import math

def find_volume_sphere(radius):
    volume = (4/3)*(math.pi)*(radius**3)
    return volume

def find_volume_cube(side):
    volume = side**3
    return volume

radius = input("Enter the gum ball radius (in.) => ")
print(radius)
sales = input("Enter the weekly sales => ")
print(sales, "\n")
radius = float(radius)

def how_many_balls(radius, sales):
    if radius == 0 and sales == 0:
        print("The machine needs to hold 0 gum balls along each edge.")
        print("Total edge length is 0.00 inches.")
        print("Target sales were 0, but the machine will hold 0 extra gum balls.")
        print("Wasted space is 0.00 cubic inches with the target number of gum balls,")
        print("or 0.00 cubic inches if you fill up the machine.")
    else:
        volume = math.ceil(float(sales)*1.25)
        dia = radius*2
        side = math.ceil(volume**(1/3))
        edgelen = side*dia
        full = side**3
        extraball = full-volume
        ballvol = find_volume_sphere(radius)
        cubevol = find_volume_cube(edgelen)
        wastedtarget = cubevol - (ballvol*volume)
        wastedfull = cubevol - (ballvol*full)
        print("The machine needs to hold", side ,"gum balls along each edge.")
        print("Total edge length is {:.02f} inches.".format(edgelen))
        print("Target sales were", str(volume) +", but the machine will hold", extraball ,"extra gum balls.")
        print("Wasted space is {:.02f}".format(wastedtarget) ,"cubic inches with the target number of gum balls,")
        print("or {:.02f}".format(wastedfull), "cubic inches if you fill up the machine.")


how_many_balls(radius,sales)

