import re

def replace_with_colon(text):
    pattern = r'[ ,.]'
    replaced_text = re.sub(pattern, ':', text)
    return replaced_text

text = "This is a test, with some spaces. And, some commas, too."

result = replace_with_colon(text)

print(result)