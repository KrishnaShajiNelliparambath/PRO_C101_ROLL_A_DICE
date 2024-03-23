import random

again=True

while again:
    num=random.randint(1,6)
    roll_again=input("Want to role the dice again?(y/n)")
    if roll_again=="y":
        if num==1:
            print("[-----]")
            print("|     |")
            print("|  0  |")
            print("|     |")
            print("[_____]")
        elif num==2:
            print("[-----]")
            print("| 0   |")
            print("|     |")
            print("|   0 |")
            print("[_____]")
        elif num==3:
            print("[-----]")
            print("| 0   |")
            print("|  0  |")
            print("|   0 |")
            print("[_____]")
        elif num==4:
            print("[-----]")
            print("| 0 0 |")
            print("|     |")
            print("| 0 0 |")
            print("[_____]")
        elif num==5:
            print("[-----]")
            print("| 0 0 |")
            print("|  0  |")
            print("| 0 0 |")
            print("[_____]")
        elif num==6:
            print("[-----]")
            print("| 0 0 |")
            print("| 0 0 |")
            print("| 0 0 |")
            print("[_____]")
    else:
        break