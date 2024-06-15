def count_occurrences(lst, element):
    return lst.count(element)

# Example usage
lst = input("Enter elements separated by spaces: ").split()
element = input("Enter the element to count: ")
print(f"The element '{element}' appears {count_occurrences(lst, element)} times.")
