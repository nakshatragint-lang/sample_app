def factorial(n: int):
    if n < 0:
        raise ValueError("Negative numbers not allowed")
    if n in (0, 1):
        return 1
    return n * factorial(n - 1)

def fibonacci(n: int):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
