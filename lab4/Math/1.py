import math

def degree_to_radian(degrees):
    radians = degrees * math.pi / 180
    return radians

def main():
    try:
        degrees = float(input())
        radians = degree_to_radian(degrees)
        print("Input degree:", degrees)
        print("Output radian:", radians)
    except ValueError:
        print( )

if __name__ == "__main__":
    main()