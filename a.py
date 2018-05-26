a=input("Press A to convert Paisa into Rupee, Press B to convert Rupee into Paisa")
if a=='A':
        b=int(input("Enter the amount of Paisa"))
        c=b/100
        print(c)
elif a=='B':
        b=int(input("Enter the amount of Rupee"))
        c=b*100
        print(c)
