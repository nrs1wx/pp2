def even_numbers_generator(n):
    for num in range(n + 1):
        if num % 2 == 0:
            yield num

def main():
    try:
        n = int(input())
        even_gen = even_numbers_generator(n)
        even_numbers = [str(num) for num in even_gen]
        print(", ".join(even_numbers))
    except ValueError:
        print( )

if __name__ == "__main__":
    main()
    