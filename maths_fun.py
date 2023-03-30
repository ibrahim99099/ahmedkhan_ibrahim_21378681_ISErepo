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





