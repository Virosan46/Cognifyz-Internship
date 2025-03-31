#The Fibonacci sequence is a type series where each number is the sum of the two that precede it. It starts from 0 and 1 usually. The Fibonacci sequence is given by 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, and so on.
def fibonacci(n):
    if n <= 0:
        print("Please enter a positive integer.")
    elif n == 1:
        return [0]  # If only one term is required, return [0].
    elif n == 2:
        return [0, 1]  # If two terms are required, return [0, 1].

    # Initialize first two terms
    fib_sequence = [0, 1]

    # Generate remaining terms
    for _ in range(n - 2):  # We already have two terms, so we generate (n-2) more
        next_term = fib_sequence[-1] + fib_sequence[-2]  # Sum of last two terms
        fib_sequence.append(next_term)

    return fib_sequence  # Return the full sequence


# Get user input
num_terms = int(input("Enter the number of terms: "))

# Print Fibonacci sequence
print("Fibonacci Sequence:", fibonacci(num_terms))
