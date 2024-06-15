def sum_of_digits(num):
    return sum(int(digit) for digit in str(num))

# Example usage
num = int(input("Enter a number: "))
print(f"The sum of the digits is: {sum_of_digits(num)}")
