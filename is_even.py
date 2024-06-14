def is_even(num):
    return num % 2 == 0

def is_odd(num):
    return num % 2 != 0

input = float(input("Enter a number:"))

print(is_odd(input))

print(is_even(input))