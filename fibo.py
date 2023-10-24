# Dictionary to store previously computed Fibonacci numbers
fib_cache = {}

def fibonacci(n):
    # Check if the Fibonacci number is already in the cache
    if n in fib_cache:
        return fib_cache[n]

    # Base case: the first two Fibonacci numbers
    if n == 0:
        return 0
    elif n == 1:
        return 1

    # Recursive case: compute Fibonacci numbers using memoization
    result = fibonacci(n - 1) + fibonacci(n - 2)

    # Store the result in the cache
    fib_cache[n] = result

    return result

# Example usage
n = 10
print(f"The {n}th Fibonacci number is: {fibonacci(n)}")
