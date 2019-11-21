for i in range (0,6):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")
for i in range (6, 0, -1):
    for j in range(0, i -2):
        print("*", end=' ')
    print("\r")
