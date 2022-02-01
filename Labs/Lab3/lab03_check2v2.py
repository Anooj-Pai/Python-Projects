
def skew(time1, time2, time3, time4, time5):
    avg = (time1 + time2 + time3 + time4 + time5) / 5
    var = (time1 - avg) ** 2 + (time2 - avg) ** 2 + (time3 - avg) ** 2 + (time4 - avg) ** 2 + (time5 - avg) ** 2
    var /= 5
    skew = (time1 - avg) ** 3 + (time2 - avg) ** 3 + (time3 - avg) ** 3 + (time4 - avg) ** 3 + (time5 - avg) ** 3
    skew /= 5
    skew = skew / var ** 3 ** 0.5
    return skew

def stats(name, time1, time2, time3, time4, time5):
    list = [time1,time2,time3,time4,time5]
    list.sort()
    minn = list[0]
    list.remove(minn)
    maxx = list[-1]
    list.remove(maxx)
    avg = sum(list)/len(list)
    print(name,"stats-- min:", minn, "max:", maxx, "avg: {:.01f}".format(avg))

print ("{0}'s running times have a skew of {1:.2f}".format("Stan",skew(34, 34, 35, 31, 29)))
print ("{0}'s running times have a skew of {1:.2f}".format("Kyle",skew(30, 31, 29, 29, 28)))
print ("{0}'s running times have a skew of {1:.2f}".format("Cartman",skew(36, 31, 32, 33, 33)))
print ("{0}'s running times have a skew of {1:.2f}".format("Kenny",skew(33, 32, 34, 31, 35)))
print ("{0}'s running times have a skew of {1:.2f}".format("Bebe",skew(27, 29, 29, 28, 30)))
print("\n")
stats("Stan",34, 34, 35, 31, 29)
stats("Kyle",30, 31, 29, 29, 28)
stats("Cartman",36, 31, 32, 33, 33)
stats("Kenny",33, 32, 34, 31, 35)
stats("Bebe",27, 29, 29, 28, 30)