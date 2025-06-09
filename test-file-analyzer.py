# Counts words, characters, or lines.

with open('sample.txt', 'r') as file:
    text = file.read()
    print("Words:", len(text.split()))
    print("Characters:", len(text))
    print("Lines:", len(text.splitlines()))
