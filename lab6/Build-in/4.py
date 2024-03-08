import time
import math

def square_root_after_milliseconds(number, milliseconds):
    time.sleep(milliseconds / 1000) 
    result = math.sqrt(number)
    print(f"Square root of {number} after {milliseconds} milliseconds is {result}")

if __name__ == "__main__":
    number = int(input("Enter the number: "))
    milliseconds = int(input("Enter the milliseconds to wait: "))
    square_root_after_milliseconds(number, milliseconds)