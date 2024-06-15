# a program that takes a string input from the user and writes it to a text file
user_input = input("Enter a string to write to a file: ")

# Step 2: Open a file in write mode ('w')
file_name = "user_input.txt"  # You can change the file name as per your choice
with open(file_name, 'w') as file:
    # Step 3: Write the user input to the file
    file.write(user_input)

# Step 4: Confirmation message
print(f"Successfully wrote the input to {file_name}")
