def bunnypop(bpop, fpop):
    bpop_next = [0,(10 * bpop) / (1 + 0.1 * bpop) - 0.05 * bpop * fpop]
    return max(bpop_next)

def foxpop(bpop, fpop):
    fpop_next = [0,0.4 * fpop + 0.02 * fpop * bpop]
    return max(fpop_next)

bpop = int(input("Number of bunnies ==> "))
print(bpop)
fpop = int(input("Number of foxes ==> "))
print(fpop)

bpop_next = int(bunnypop(bpop,fpop))
fpop_next = int(foxpop(bpop, fpop))
print("Year 1: ", bpop, fpop)
print("Year 2: ", bpop_next, fpop_next)
bpop = bpop_next
fpop = fpop_next
bpop_next = int(bunnypop(bpop,fpop))
fpop_next = int(foxpop(bpop, fpop))
print("Year 3: ", bpop_next, fpop_next)
bpop = bpop_next
fpop = fpop_next
bpop_next = int(bunnypop(bpop,fpop))
fpop_next = int(foxpop(bpop, fpop))
print("Year 4: ", bpop_next, fpop_next)
bpop = bpop_next
fpop = fpop_next
bpop_next = int(bunnypop(bpop,fpop))
fpop_next = int(foxpop(bpop, fpop))
print("Year 5: ", bpop_next, fpop_next)