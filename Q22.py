def min_max(lst):
    return min(lst), max(lst)

# Example usage
lst = list(map(int, input("Enter numbers separated by spaces: ").split()))
min_val, max_val = min_max(lst)
print(f"The minimum value is: {min_val}, and the maximum value is: {max_val}")
