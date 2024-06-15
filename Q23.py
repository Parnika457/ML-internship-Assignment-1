def celsius_to_fahrenheit(c):
    return c * 9/5 + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

# Example usage
choice = input("Convert from (C)elsius or (F)ahrenheit? ").upper()
temperature = float(input("Enter the temperature: "))

if choice == 'C':
    print(f"{temperature}°C is {celsius_to_fahrenheit(temperature):.2f}°F")
elif choice == 'F':
    print(f"{temperature}°F is {fahrenheit_to_celsius(temperature):.2f}°C")
else:
    print("Invalid choice!")
