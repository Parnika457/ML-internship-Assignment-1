#a program that reads the content of a text file and prints it to the console.
def read_and_print_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("The file does not exist.")

# Example usage
file_path = "example.txt"  # Replace with your file path
read_and_print_file(file_path)
