# =========================================
# 1. Arbitrary Arguments (*args, **kwargs)
# =========================================

# Practice Problem 1
# Average of numbers using *args

def average_marks(*marks):

    avg = sum(marks) / len(marks)

    print("Average:", avg)

average_marks(80, 90, 75, 85)


# Practice Problem 2
# Subjects and student details

def student_details(*subjects, **info):

    print("Subjects:")

    for sub in subjects:
        print(sub)

    print("\nStudent Details:")

    for key, value in info.items():
        print(f"{key}: {value}")

student_details(
    "Maths",
    "Physics",
    "Chemistry",
    name="Aravind",
    age=21,
    grade="A",
    section="CSE-A"
)


# Practice Problem 3
# Product names and metadata

def product_info(*products, **details):

    print("Products:")

    for p in products:
        print(p)

    print("\nDetails:")

    for key, value in details.items():
        print(f"{key}: {value}")

product_info(
    "Laptop",
    "Mouse",
    "Keyboard",
    category="Electronics",
    brand="Dell",
    price_range="20000-80000",
    availability="In Stock"
)



# =========================================
# 2. Pure Functions
# =========================================

# Practice Problem 1
# Celsius to Fahrenheit

def celsius_to_fahrenheit(temp_list):

    return [(t * 9/5) + 32 for t in temp_list]

print(celsius_to_fahrenheit([20, 25, 30]))


# Practice Problem 2
# Cube of each number

def cube_list(numbers):

    return [n ** 3 for n in numbers]

print(cube_list([1, 2, 3, 4]))


# Practice Problem 3
# Even or Odd

def even_or_odd(num):

    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(even_or_odd(7))



# =========================================
# 3. Returning Multiple Values
# =========================================

# Practice Problem 1
# Sum and Average

def sum_and_average(numbers):

    total = sum(numbers)
    avg = total / len(numbers)

    return total, avg

total, avg = sum_and_average([80, 90, 70, 60])

print("Sum:", total)
print("Average:", avg)


# Practice Problem 2
# Quotient and Remainder

def divide_numbers(a, b):

    quotient = a // b
    remainder = a % b

    return quotient, remainder

q, r = divide_numbers(17, 5)

print("Quotient:", q)
print("Remainder:", r)


# Practice Problem 3
# Square and Cube

def square_cube(n):

    return n ** 2, n ** 3

square, cube = square_cube(4)

print("Square:", square)
print("Cube:", cube)



# =========================================
# 4. Recursive Functions
# =========================================

# Practice Problem 1
# Sum from 1 to n

def sum_n(n):

    if n == 1:
        return 1

    return n + sum_n(n - 1)

print(sum_n(5))


# Practice Problem 2
# Print numbers from n to 1

def print_reverse(n):

    if n == 0:
        return

    print(n)

    print_reverse(n - 1)

print_reverse(5)


# Practice Problem 3
# Power of a number

def power(x, n):

    if n == 0:
        return 1

    return x * power(x, n - 1)

print(power(2, 4))