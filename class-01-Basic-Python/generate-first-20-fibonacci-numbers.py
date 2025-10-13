# Generate and print the first 12 Fibonacci numbers

def generate_fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

first_n_fibonacci = generate_fibonacci(20)
print(first_n_fibonacci)