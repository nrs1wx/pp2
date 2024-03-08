import os

def list_directories_and_files(path):
    print("Directories:")
    for item in os.listdir(path):
        if os.path.isdir(os.path.join(path, item)):
            print(item)

    print("\nFiles:")
    for item in os.listdir(path):
        if os.path.isfile(os.path.join(path, item)):
            print(item)

def list_all_directories_and_files(path):
    for root, directories, files in os.walk(path):
        print("Current Directory:", root)
        print("Directories:")
        for directory in directories:
            print(os.path.join(root, directory))
        print("\nFiles:")
        for file in files:
            print(os.path.join(root, file))
        print()

if __name__ == "__main__":
    path = input("Enter the path: ")
    
    print("\nListing directories and files:")
    list_directories_and_files(path)

    print("\nListing all directories and files:")
    list_all_directories_and_files(path)