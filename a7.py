# 1. Square Pattern

n = 5

for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()


# 2. Hollow Square Pattern

n = 5

for i in range(n):
    for j in range(n):

        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()


# 3. Rectangle Pattern

rows = 4
cols = 6

for i in range(rows):
    for j in range(cols):
        print("*", end=" ")
    print()


# 4. Hollow Rectangle Pattern

rows = 4
cols = 6

for i in range(rows):
    for j in range(cols):

        if i == 0 or i == rows-1 or j == 0 or j == cols-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()


# 5. Right Angle Triangle Left Aligned

n = 5

for i in range(1, n+1):
    for j in range(i):
        print("*", end=" ")
    print()

# Inverse Left Aligned Triangle

for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()


# 6. Hollow Right Angle Triangle Left Aligned

n = 5

for i in range(1, n+1):

    for j in range(1, i+1):

        if j == 1 or j == i or i == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()

# Inverse Hollow Left Aligned Triangle

for i in range(n, 0, -1):

    for j in range(1, i+1):

        if j == 1 or j == i or i == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()


# 7. Right Angle Triangle Right Aligned

n = 5

for i in range(1, n+1):

    for j in range(n-i):
        print(" ", end=" ")

    for k in range(i):
        print("*", end=" ")

    print()

# Inverse Right Aligned Triangle

for i in range(n, 0, -1):

    for j in range(n-i):
        print(" ", end=" ")

    for k in range(i):
        print("*", end=" ")

    print()


# 8. Hollow Right Angle Triangle Right Aligned

n = 5

for i in range(1, n+1):

    for j in range(n-i):
        print(" ", end=" ")

    for k in range(1, i+1):

        if k == 1 or k == i or i == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()

# Inverse Hollow Right Aligned Triangle

for i in range(n, 0, -1):

    for j in range(n-i):
        print(" ", end=" ")

    for k in range(1, i+1):

        if k == 1 or k == i or i == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()