import random
x = "y"
while x == "y":
    a = random.randint(1,6)
    if a == 1:
        print("----------")
        print("|        |")
        print("|   0    |")
        print("|        |")
        print("----------")
    if a == 3:
        print("----------")
        print("|       0|")
        print("|    0   |")
        print("|0       |")
        print("----------")

    if a == 2:
        print("----------")
        print("|       0|")
        print("|        |")
        print("|0       |")
        print("----------")

    if a == 4:
        print("----------")
        print("|0      0|")
        print("|        |")
        print("|0      0|")
        print("----------")

    if a == 5:
        print("---------")
        print("|0     0|")
        print("|   0   |")
        print("|0     0|")
        print("---------")

    if a == 6:
        print("----------")
        print("|0      0|")
        print("|0      0|")
        print("|0      0|")
        print("----------")


    x=input("y")
