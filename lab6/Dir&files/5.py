def write_list_to_file(file_path, data):
    try:
        with open(file_path, 'w') as file:
            for item in data:
                file.write(str(item) + '\n')
        print(f"List successfully written to '{file_path}'.")
    except IOError:
        print(f"Unable to write to file '{file_path}'.")

if __name__ == "__main__":
    data = ['apple', 'banana', 'cherry', 'date']
    file_path = input("Enter the path to the file: ")
    write_list_to_file(file_path, data)
