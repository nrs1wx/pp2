def parallelogram_area(base, height):
    area = base * height
    return area

def main():
    try:
        base = float(input("Length of base: "))
        height = float(input("Height of parallelogram: "))
        area = parallelogram_area(base, height)
        print("Expected Output:", area)
    except ValueError:
        print( )

if __name__ == "__main__":
    main()