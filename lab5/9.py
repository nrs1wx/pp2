import re

def insert_spaces(text):
    modified_text = re.sub(r'(?<!^)(?=[A-Z])', ' ', text)
    return modified_text

text = "InsertSpacesBetweenWordsStartingWithCapitalLetters"

result = insert_spaces(text)

print(result)