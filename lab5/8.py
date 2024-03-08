import re

def split_at_uppercase(text):
    split_text = re.split(r'(?=[A-Z])', text)
    return split_text

text = "SplitThisStringAtUppercaseLetters"

result = split_at_uppercase(text)

print(result)