import re

def match_string(pattern, text):
    match = re.match(pattern, text)
    
    if match:
        print("Match found:", match.group())
    else:
        print("No match found")

pattern = r'a*b*'

test_strings = ["ab", "abb", "aab", "a", "b", "bb", "abbb"]

for text in test_strings:
    print("Testing:", text)
    match_string(pattern, text)