# Function to print Fibonacci sequence
def fibonacci(n):
    a, b = 0, 1
    sequence = []
    while len(sequence) < n:
        sequence.append(a)
        a, b = b, a + b
    return sequence

terms = 10
sequence = fibonacci(terms)
print(f"The first {terms} terms of the Fibonacci sequence are: {sequence}")
