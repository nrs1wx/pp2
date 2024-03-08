def countdown_generator(n):
    while n >= 0:
        yield n
        n -= 1

def main():
    try:
        n = int(input())
        for num in countdown_generator(n):
            print(num)
    except ValueError:
        print( )

if __name__ == "__main__":
    main()