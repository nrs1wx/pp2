import re

def find_sequences(text):
    pattern = r'[A-Z][a-z]+'
    sequences = re.findall(pattern, text)
    return sequences

text = "This is a Test string With Multiple sequences Like This one Or This Example"

result = find_sequences(text)

if result:
    print("Sequences:")
    for seq in result:
        print(seq)
else:
    print("No sequences")