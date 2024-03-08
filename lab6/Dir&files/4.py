def count_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            line_count = sum(1 for line in file)
        print(f"Number of lines in '{file_path}': {line_count}")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except IOError:
        print(f"Unable to read file '{file_path}'.")

if __name__ == "__main__":
    file_path = input("Enter the path to the text file: ")
    count_lines(file_path)