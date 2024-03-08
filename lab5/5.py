import re

def match_string(pattern, text):
    match = re.match(pattern, text)
    
    if match:
        print("Match:", match.group())
    else:
        print("No match")

pattern = r'a.*b$'

test_strings = ["axb", "a1234b", "ab", "acb", "aB", "aBb", "aabb", "abbbb", "a_b"]

for text in test_strings:
    print(text)
    match_string(pattern, text)