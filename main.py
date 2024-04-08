"""
OrderOfNumbers
"""

while True:
    n1 = int(input("n1: "))
    n2 = int(input("n2: "))
    n3 = int(input("n3: "))
    if n1 < n2 < n3:
        print("numbers are ascending")
    elif n1 > n2 > n3:
        print("numbers are descending")
    else:
        if n1 % 2 == 0 and n2 % 2 == 0 and n3 % 2 == 0:
            print("no specific order, but all even")
        elif n1 % 2 != 0 and n2 % 2 != 0 and n3 % 2 != 0:
            print("no specific order, but all odd")
        else:
            print("no specific order")




"""
SumUp
"""
n1 = int(input("n1: "))
n2 = int(input("n2: "))


if n2 <= 0 and n1 <= 0:
    print("n1 and n2 need to be > 0")

elif n1 <= 0:
    print("n1 needs to be > 0")

elif n2 <= 0:
    print("n2 needs to be > 0")

elif n2 < n1:  # I didn't include  "n1 > 0 and n2 > 0" in this statement because it's already checked for before
    print("n2 needs to be > n1")


else:
    i = 0
    while n1 + i <= n2:
        print(n1 + i, " ", end="")
        i += 1


