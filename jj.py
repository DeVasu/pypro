"""import random as ran
from math import pi
"""
a=[0, 1, 2, 9]
print (a[0])
print (a[1])
print(9 in a)

b={"Me":45, "Ne":45}
print (b["Me"])
print (b["Ne"])
print(45 in b)
print("Me" in b)

c=("this", "is", "a",("nested", "tuple", "iss", "here") ,'tuple')
print(c[0])
print(c[3][0])

d=[i for i in range(30) if not i%2==0]
print(d)

msg="thisis is fjlj {0} {1} {2}".format(d[0], d[1], d[2])
print(msg)

for i in c:
    print (i)
