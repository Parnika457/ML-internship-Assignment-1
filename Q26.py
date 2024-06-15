def check_prefix_suffix(s, prefix, suffix):
    return s.startswith(prefix), s.endswith(suffix)

# Example usage
s = input("Enter a string: ")
prefix = input("Enter the prefix to check: ")
suffix = input("Enter the suffix to check: ")

starts_with, ends_with = check_prefix_suffix(s, prefix, suffix)
print(f"Starts with '{prefix}': {starts_with}")
print(f"Ends with '{suffix}': {ends_with}")
