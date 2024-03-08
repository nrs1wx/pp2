import re

def find_sequences(text):
    pattern = r'[a-z]+_[a-z]+'
    sequences = re.findall(pattern, text)
    return sequences
text = "This_is_a_test_string_with_multiple_sequences_like_this_one_or_this_example"

result = find_sequences(text)

if result:
    print("Sequences:")
    for seq in result:
        print(seq)
else:
    print("No sequences")