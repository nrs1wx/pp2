def all_true(tup):
    return all(tup)

if __name__ == "__main__":
    my_tuple = (True, True, False, True)
    print("All elements are true." if all_true(my_tuple) else "Not all elements are true.")