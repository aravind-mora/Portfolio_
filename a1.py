# 1. Check Even or Odd
num = 6

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")


# 2. Divisible by 5 but Not by 10
num = 25

if num % 5 == 0 and num % 10 != 0:
    print("Satisfy")
else:
    print("Not Satisfy")


# 3. Biggest Among Two Numbers
a = 4
b = 7

if a > b:
    print("Biggest is:", a)
else:
    print("Biggest is:", b)


# 4. Smallest Among Two Numbers
a = 4
b = 7

if a < b:
    print("Smallest is:", a)
else:
    print("Smallest is:", b)


# 5. Divisible by 2, 3, and 6
num = 18

if num % 2 == 0 and num % 3 == 0 and num % 6 == 0:
    print("Satisfy")
else:
    print("Not Satisfy")


# 6. Voting Eligibility
age = 19

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")


# 7. Student Pass/Fail Based on All Subjects >= 35
maths = 40
physics = 36
chemistry = 30

if maths >= 35 and physics >= 35 and chemistry >= 35:
    print("Pass")
else:
    print("Fail")


# 8. Student Pass if Passed Any One Subject
maths = 20
physics = 38
chemistry = 25

if maths >= 35 or physics >= 35 or chemistry >= 35:
    print("Pass")
else:
    print("Fail")


# 9. Student Pass if Passed Any Two Subjects
maths = 40
physics = 20
chemistry = 36

count = 0

if maths >= 35:
    count += 1
if physics >= 35:
    count += 1
if chemistry >= 35:
    count += 1

if count >= 2:
    print("Pass")
else:
    print("Fail")


# 10. Biggest Among Three Numbers
a = 7
b = 4
c = 9

if a > b and a > c:
    print("Biggest is:", a)
elif b > a and b > c:
    print("Biggest is:", b)
else:
    print("Biggest is:", c)


# 11. Smallest Among Three Numbers
a = 7
b = 4
c = 9

if a < b and a < c:
    print("Smallest is:", a)
elif b < a and b < c:
    print("Smallest is:", b)
else:
    print("Smallest is:", c)


# 12. Perfect Square or Not
num = 49

root = int(num ** 0.5)

if root * root == num:
    print("Perfect square")
else:
    print("Not a perfect square")


# 13. Cars Required for Members (Max 5 per car)
members = 17

cars = members // 5

if members % 5 != 0:
    cars += 1

print("Cars needed =", cars)


# 14. Second Biggest Among Three Numbers
a = 10
b = 25
c = 18

if (a > b and a < c) or (a < b and a > c):
    print("Second biggest:", a)
elif (b > a and b < c) or (b < a and b > c):
    print("Second biggest:", b)
else:
    print("Second biggest:", c)


# 15. Leap Year or Not
year = 2024

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")