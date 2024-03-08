def camel_to_snake(camel_case):
    snake_case = ''
    for char in camel_case:
        if char.isupper():
            snake_case += '_' + char.lower()
        else:
            snake_case += char
    if snake_case.startswith('_'):
        snake_case = snake_case[1:]
    return snake_case

camel_case_string = "thisIsCamelSample"
snake_case_string = camel_to_snake(camel_case_string)
print(snake_case_string)