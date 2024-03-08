def trapezoid_area(height, base1, base2):
    area = (base1 + base2) * height / 2
    return area

def main():
    try:
        height = float(input("Height: "))
        base1 = float(input("Base, first value: "))
        base2 = float(input("Base, second value: "))
        area = trapezoid_area(height, base1, base2)
        print("Expected Output:", area)
    except ValueError:
        print( )

if __name__ == "__main__":
    main()