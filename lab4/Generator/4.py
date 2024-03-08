def squares(a, b):
    for num in range(a, b + 1):
        yield num ** 2

def main():
    try:
        a = int(input())
        b = int(input())
    
        for square in squares(a, b):
            print(square)
    except ValueError:
        print( )

if __name__ == "__main__":
    main()