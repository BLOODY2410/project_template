import pandas as pd

def get_text_input():
    """Reads a line of text from console input."""
    return input("Enter some text: ")

def read_file_builtin(file_path):
    """Reads text content from a file using built-in Python open()."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return "File not found."

def read_file_pandas(file_path):
    """Reads a file using pandas and returns it as string."""
    try:
        df = pd.read_csv(file_path)
        return df.to_string()
    except Exception as e:
        return f"Error reading with pandas: {e}"
