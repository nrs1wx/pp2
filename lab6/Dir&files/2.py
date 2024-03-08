import os

def check_path_access(path):

    if not os.path.exists(path):
        print(f"The path '{path}' does not exist.")
        return

    if os.access(path, os.R_OK):
        print(f"Read access to '{path}' is granted.")
    else:
        print(f"No read access to '{path}'.")

    if os.access(path, os.W_OK):
        print(f"Write access to '{path}' is granted.")
    else:
        print(f"No write access to '{path}'.")

    if os.access(path, os.X_OK):
        print(f"Execute access to '{path}' is granted.")
    else:
        print(f"No execute access to '{path}'.")


if __name__ == "__main__":
    path = input("Enter the path to check access: ")
    check_path_access(path)