from app.io.input import get_text_input, read_file_builtin, read_file_pandas
from app.io.output import print_to_console, write_to_file

def main():
    text1 = get_text_input()
    text2 = read_file_builtin("data/input.txt")
    text3 = read_file_pandas("data/input.csv")

    print_to_console(text1)
    print_to_console(text2)
    print_to_console(text3)

    write_to_file(text1 + "\n\n" + text2 + "\n\n" + text3, "data/output.txt")

if __name__ == "__main__":
    main()
