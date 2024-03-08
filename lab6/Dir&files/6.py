import string

def generate_text_files():
    for letter in string.ascii_uppercase:
        file_name = letter + ".txt"
        with open(file_name, 'w') as file:
            file.write(f"This is file {file_name}.\n")

if __name__ == "__main__":
    generate_text_files()
    print("Text files generated successfully.")