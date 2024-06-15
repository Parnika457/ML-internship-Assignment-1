def read_lines_until_empty():
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    return "\n".join(lines)

# Example usage
print("Enter lines (press Enter on an empty line to finish):")
print(read_lines_until_empty())
