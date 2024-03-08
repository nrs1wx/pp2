from functools import reduce

def multiply_list(numbers):
    result = reduce(lambda x, y: x * y, numbers)
    return result

if __name__ == "__main__":
    numbers = [2, 3, 4, 5, 6]
    product = multiply_list(numbers)
    print("Product of all numbers:", product)