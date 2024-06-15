def calculate_age(birth_year):
    from datetime import date
    current_year = date.today().year
    return current_year - birth_year

# Example usage
birth_year = int(input("Enter your birth year: "))
print(f"Your age is: {calculate_age(birth_year)}")
