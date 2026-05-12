# Date: 6/11/25
# Nested Loops Problems


# 1. Multiplication tables from 1 to 10

for i in range(1, 11):
    print("Table of", i)

    for j in range(1, 11):
        print(i, "x", j, "=", i * j)

    print()


# 2. Add two 2D lists (matrices)

a = [
    [1, 2],
    [3, 4]
]

b = [
    [5, 6],
    [7, 8]
]

result = []

for i in range(len(a)):
    row = []

    for j in range(len(a[0])):
        row.append(a[i][j] + b[i][j])

    result.append(row)

print("Matrix Addition:")
for row in result:
    print(row)


# 3. Count even and odd numbers in nested list

nested = [
    [1, 2, 3],
    [4, 5, 6]
]

even = 0
odd = 0

for row in nested:
    for num in row:

        if num % 2 == 0:
            even += 1
        else:
            odd += 1

print("Even:", even)
print("Odd:", odd)


# 4. Prime numbers between 2 and 50

print("Prime Numbers:")

for num in range(2, 51):

    prime = True

    for i in range(2, num):

        if num % i == 0:
            prime = False
            break

    if prime:
        print(num)


# 5. Transpose of a matrix

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

transpose = []

for i in range(len(matrix[0])):

    row = []

    for j in range(len(matrix)):
        row.append(matrix[j][i])

    transpose.append(row)

print("Transpose Matrix:")

for row in transpose:
    print(row)


# 6. Unique pair combinations

lst = [1, 2, 3, 4]

print("Unique Pairs:")

for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        print(lst[i], lst[j])


# 7. Common characters in two strings

str1 = "python"
str2 = "typhoon"

print("Common Characters:")

for ch1 in str1:
    for ch2 in str2:

        if ch1 == ch2:
            print(ch1)
            break


# 8. Count vowels in each word

words = ["python", "apple", "education"]

vowels = "aeiou"

for word in words:

    count = 0

    for ch in word:

        for v in vowels:

            if ch.lower() == v:
                count += 1

    print(word, "=", count)


# 9. Common elements between two lists

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

print("Common Elements:")

for i in list1:
    for j in list2:

        if i == j:
            print(i)


# 10. Sum of elements in each row of 2D list

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Row Sums:")

for row in matrix:

    total = 0

    for num in row:
        total += num

    print(total)