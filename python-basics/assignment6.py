#Name: Valentine Kimani
#Date: 17/02/2026
#Program to display a diamond and triangle pattern using asterisks

# Diamond pattern
for i in range(5):
    for j in range(5 - i):
        print(" ", end="")
    for k in range(2 * i + 1):
        print("*", end="")
    print()