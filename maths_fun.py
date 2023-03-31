def fibonacci(n):
    if n < 0:
        print(f"{n} is not in the Fibonacci sequence (negative numbers are not in the sequence)")
    elif n == 0:
        print(f"{n} is in the Fibonacci sequence")
    else:
        a, b = 0, 1
        while b < n:
            a, b = b, a + b
        if b == n:
            print(f"{n} is in the Fibonacci sequence")
        else:
            print(f"{n} is not in the Fibonacci sequence")

def closefibonacci(n):
    fibonacci(n)
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    if b != n:
        print(f"The next larger number in the Fibonacci sequence is {b}")

def is_integer(n):
    try:
        num = int(n)
        return True
    except ValueError:
        return False

def check_fibonacci_numbers(filename):
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




