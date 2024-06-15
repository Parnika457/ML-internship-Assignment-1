def fibonacci(n):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:n]

# Example usage
n = int(input("Enter the number of Fibonacci numbers to generate: "))
print(f"The first {n} Fibonacci numbers are: {fibonacci(n)}")
