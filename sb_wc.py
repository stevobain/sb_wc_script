import sys

def count_bytes(data, from_file=True):
    if from_file:
        with open(data, 'rb') as file:
            content = file.read()
    else:
        content = data.encode()
    return len(content)

def count_lines(data, from_file=True):
    if from_file:
        with open(data, 'r') as file:
            content = file.readlines()
    else:
        content = data.splitlines()
    return len(content)

def count_words(data, from_file=True):
    if from_file:
        with open(data, 'r') as file:
            content = file.read()
    else:
        content = data
    return len(content.split())

def count_characters(data, from_file=True):
    if from_file:
        with open(data, 'r', encoding='utf-8') as file:
            content = file.read()
    else:
        content = data
    return len(content)

# Command-line argument parsing
if __name__ == "__main__":
    option = ""  # Initialize option

    if len(sys.argv) == 1 or (len(sys.argv) == 2 and sys.argv[1] in ["-c", "-l", "-w", "-m"]):
        # Read from stdin if no filename is specified
        input_data = sys.stdin.read()
        from_file = False
        if len(sys.argv) == 2:
            option = sys.argv[1]
    else:
        if len(sys.argv) == 3:
            option = sys.argv[1]
            file_path = sys.argv[2]
        else:
            file_path = sys.argv[1]
        input_data = file_path
        from_file = True

    byte_count = count_bytes(input_data, from_file)
    line_count = count_lines(input_data, from_file)
    word_count = count_words(input_data, from_file)
    char_count = count_characters(input_data, from_file)

    if option == "-c":
        print(f"{byte_count} bytes")
    elif option == "-l":
        print(f"{line_count} lines")
    elif option == "-w":
        print(f"{word_count} words")
    elif option == "-m":
        print(f"{char_count} characters")
    else:
        print(f"{line_count} lines, {word_count} words, {byte_count} bytes")
