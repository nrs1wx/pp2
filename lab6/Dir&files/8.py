import os

def check_path_access(path):
    if os.path.exists(path):
        print("Path exists.")

        if os.access(path, os.F_OK):
            print("Access granted.")
            return True
        else:
            print("No access to the specified path.")
            return False
    else:
        print("Path does not exist.")
        return False

def delete_file(file_path):
    if check_path_access(file_path):
        try:
            os.remove(file_path)
            print(f"File '{file_path}' deleted successfully.")
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
        except PermissionError:
            print(f"Error: Permission denied for file '{file_path}'.")

if __name__ == "__main__":
    file_path = input("Enter the path of the file to delete: ")
    delete_file(file_path)