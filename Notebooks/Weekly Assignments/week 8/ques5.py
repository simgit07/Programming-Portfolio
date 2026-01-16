import sys
import re

def load_dictionary(dict_file):
    with open(dict_file, 'r') as f:
        return set(word.strip().lower() for word in f)

def spellcheck(filename, dictionary):
    with open(filename, 'r') as f:
        text = f.read().lower()

    words = re.findall(r"[a-z]+", text)

    misspelled = set(word for word in words if word not in dictionary)

    for word in sorted(misspelled):
        print(word)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python spell.py <filename> <dictionary>")
        sys.exit(1)

    dictionary = load_dictionary(sys.argv[2])
    spellcheck(sys.argv[1], dictionary)
