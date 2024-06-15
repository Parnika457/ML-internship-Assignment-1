from collections import Counter

def character_frequency(s):
    return Counter(s)

# Example usage
s = input("Enter a string: ")
print(f"Character frequencies: {character_frequency(s)}")
