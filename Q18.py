def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)

# Example usage
s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")
print(f"Are the strings anagrams? {are_anagrams(s1, s2)}")
