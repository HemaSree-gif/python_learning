n = 8
for row in range (n):
    for col in range (n):
        if row == col or col == n - row - 1 or row == n // 2 or col == n //2:
            print("*", end=" ")
        else :
            print(" ", end=" ")           
    print()