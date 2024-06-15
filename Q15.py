import csv

def read_and_print_csv(file_path):
    try:
        with open(file_path, mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                print(', '.join(row))
    except FileNotFoundError:
        print("The file does not exist.")

# Example usage
file_path = "example.csv"  # Replace with your file path
read_and_print_csv(file_path)
