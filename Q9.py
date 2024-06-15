def is_substring_present(main_string, substring):
    return substring in main_string

# Example usage
main_string = input("Enter the main string: ")
substring = input("Enter the substring: ")
print(f"Is the substring present? {is_substring_present(main_string, substring)}")
