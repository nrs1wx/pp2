import re

def match_string(pattern, text):
    match = re.match(pattern, text)
    
    if match:
        print(match.group())
    else:
        print("No match")

pattern = r'ab{2,3}'

test_strings = ["abb", "abbb", "abbbb", "a", "b", "ab", "aabb", "aabbb", "aabbbb"]

for text in test_strings:
    print(text)
    match_string(pattern, text)