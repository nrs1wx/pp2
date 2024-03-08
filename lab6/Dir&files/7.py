def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as source:
            with open(destination_file, 'w') as destination:
                for line in source:
                    destination.write(line)
        print(f"Contents of '{source_file}' copied to '{destination_file}' successfully.")
    except FileNotFoundError:
        print(f"Error: File '{source_file}' not found.")
    except IOError:
        print(f"Error: Unable to read '{source_file}' or write to '{destination_file}'.")

if __name__ == "__main__":
    source_file = input("Enter the path to the source file: ")
    destination_file = input("Enter the path to the destination file: ")
    copy_file(source_file, destination_file)