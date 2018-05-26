print("This is a Calculator")
a=int(input("What do you want to do \n Add\nSubtract\nMuliply\ndivide\nQuit"))
b=int(input("enter the first number"))
c=int(input("enter the second number"))
d=True
while True:
    if a==1:
        print(b+c)
    elif a==2:
        print(b-c)
    elif a==3:
        print(b*c)
    elif a==4:
        print(b/c)
    elif a==5:
        print("You are quitting this program")
    break
