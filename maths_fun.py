import math

def fibonacci(n):
    if n < 0:
        print (f"{n} is not in the Fibonacci sequence (negative numbers are not in the sequence)")
    elif n == 0:
        print (f"{n} is in the Fibonacci sequence")
    else:
        a, b = 0, 1
        while b < n:
            a, b = b, a + b
        if b == n:
            print (f"{n} is in the Fibonacci sequence")
        else:
            print (f"{n} is not in the Fibonacci sequence")

def closefibonacci(n):
    fibonacci(n)
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    if b != n:
        print(f"The next larger number in the Fibonacci sequence is {b}")

def is_integer(i):
    try:
        num = int(i)
        return True
    except ValueError:
        return False

def fibonacciseq(filename):
    """Reads a file containing a series of numbers and checks which ones are in the Fibonacci sequence"""
    fib_numbers = []
    non_fib_numbers = []
    try:
        with open(filename) as file:
            numbers = file.read().split()
            for num in numbers:
                num = int(num)
                if num < 0:
                    non_fib_numbers.append(num)
                else:
                    a, b = 0, 1
                    while b < num:
                        a, b = b, a + b
                    if b == num:
                        fib_numbers.append(num)
                    else:
                        non_fib_numbers.append(num)
    except OSError:
        print(f"Error reading file {filename}")
    return fib_numbers, non_fib_numbers

def issquare():
    """
    Checks if a given number is a square number or not.

    Args:
    n (int): The number to check.

    Returns:
    bool: True if n is a square number, False otherwise.
    """
    n = int(input())
    if n < 0:
        return False
    elif n == 0:
        return True
    else:
        root = math.isqrt(n)
        return root**2 == n

def issquare_and_fibonacci():
    n = int(input())
    if n < 0:
        return f"{n} is not a valid input"


    if n == 0:
        return f"{n} is a square number and in the Fibonacci sequence"

    root = math.isqrt(n)
    if root ** 2 != n:
        return f"{n} is not a square number"

    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    if b == n:
        return f"{n} is a square number and in the Fibonacci sequence"
    else:
        return f"{n} is a square number but not in the Fibonacci sequence"

def grading():
    score = int(input())
    if score <0 or score >100:
        return "Invalid score"
    elif score >= 91:
        return "Brilliant"
    elif score >= 80:
        return "Excellent"
    elif score >= 50:
        return "Great"
    elif score >= 20:
        return "Good"
    else:
        return "You can do better"

def sumeven(numbers):
    try:
        evenNumbers = [n for n in numbers if n % 2 == 0]
        return sum(evenNumbers)
    except TypeError:
        return ("Error: Input must be a list of integers.")


