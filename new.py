import math


def get_number(prompt):
    while True:
        num = input(prompt)
        try:
            return float(num)
        except ValueError:
            print("Invalid input. Please enter a number.")

def add(m, n):
    return f'{m} + {n} = {m + n}.'

def subtract(m, n):
    return f'{m} - {n} = {m - n}.'

def multiply(m, n):
    return f'{m} exponential {n} = {m * n}.'

def divide(m, n):
    if n == 0:
        return "Cannot be divided!"
    return f'{m}/{n} = {m / n}'

def exponent(m, n):
    return f'{m}**{n} = {math.pow(m, n)}.'

def modulo(m, n):
    return f'The modulo of {m} and {n} is {m % n}.'

def floor_division(m, n):
    return f'The floor division of {m} by {n} is {m // n}.'

def square(m):
    return f'The square of {m} is {math.pow(m, 2)}.'

def square_root(m):
    return f'The square root of {m} is {math.sqrt(m)}.'


def calculator():

    while True:

        print("""
        (a) Add
        (b) Subtract
        (c) Multiply
        (d) Divide
        (e) Exponent
        (f) Modulo
        (g) Floor Division
        (h) Square
        (i) Square Root
        (j) Exit""")

        choice = input("Enter choice: ").strip().lower()

        if choice == 'j':
            print("Ending Process...")
            print('*' * 15)
            break

        if choice in ['h', 'i']:
            num1 = get_number("Enter the first number: ")
            if choice == 'h':
                print(square(num1))
                print('*' * 15)

            elif choice == 'i':
                print(square_root(num1))
                print('*' * 15)

            continue

        elif choice in ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
            num1 = get_number("Enter the first number: ")
            num2 = get_number("Enter the second number: ")

            if choice == 'a':
                print(add(num1, num2))
                print('*' * 15)

            elif choice == 'b':
                print(subtract(num1, num2))
                print('*' * 15)

            elif choice == 'c':
                print(multiply(num1, num2))
                print('*' * 15)

            elif choice == 'd':
                print(divide(num1, num2))
                print('*' * 15)

            elif choice == 'e':
                print(exponent(num1, num2))
                print('*' * 15)

            elif choice == 'f':
                print(modulo(num1, num2))
                print('*' * 15)

            elif choice == 'g':
                print(floor_division(num1, num2))
                print('*' * 15)

            else:
                print("The operation isn't supported.")

        else:
            print("Operation not found. Please try again.")


calculator()
