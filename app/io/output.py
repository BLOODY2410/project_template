def print_to_console(text):
    """Prints given text to the console."""
    print(text)

def write_to_file(text, file_path):
    """Writes text to a file using built-in open()."""
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(text)
