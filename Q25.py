def copy_file(source, destination):
    try:
        with open(source, 'r') as src, open(destination, 'w') as dest:
            content = src.read()
            dest.write(content)
        print("File copied successfully.")
    except FileNotFoundError:
        print("Source file not found.")

# Example usage
source = "source.txt"  # Replace with your source file path
destination = "destination.txt"  # Replace with your destination file path
copy_file(source, destination)
