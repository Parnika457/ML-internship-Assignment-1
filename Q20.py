def sum_of_list(numbers):
    return sum(numbers)

# Example usage
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
print(f"The sum of the list is: {sum_of_list(numbers)}")
