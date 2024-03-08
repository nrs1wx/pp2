import os

def test_path(path):
    if os.path.exists(path):
        print("Path exists.")

        directory, filename = os.path.split(path)
        print("Directory:", directory)
        print("Filename:", filename)
    else:
        print("Path does not exist.")

if __name__ == "__main__":
    path = input("Enter the path to test: ")
    test_path(path)