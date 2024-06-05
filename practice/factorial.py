def factorial_with_loop(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    result = 1
    for i in range(1, n + 1):
        result *= i
    print(f"Factorial of {n} is: {result}")

def factorial_with_recursion(n, original_n=None):
    if original_n is None:
        original_n = n
    if n < 0:
        print("Factorial is not defined for negative numbers")
        return
    if n == 0 or n == 1:
        result = 1
    else:
        result = n * factorial_with_recursion(n - 1, original_n)
    if n == original_n:
        print(f"Factorial of {n} is: {result}")
    return result

