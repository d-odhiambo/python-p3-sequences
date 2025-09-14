#!/usr/bin/env python3

# sequences.py

def print_fibonacci(n):
    """Print the Fibonacci sequence up to length n."""
    fib_seq = []
    a, b = 0, 1
    for _ in range(n):
        fib_seq.append(a)
        a, b = b, a + b
    print(fib_seq)

    