import string

def remove_punctuation(s):
    return s.translate(str.maketrans('', '', string.punctuation))

# Example usage
s = input("Enter a string: ")
print(f"String without punctuation: {remove_punctuation(s)}")
