def letters_in_either(word1, word2):
    return sorted(set(word1) | set(word2))

def letters_in_both(word1, word2):
    return sorted(set(word1) & set(word2))

def letters_in_one_only(word1, word2):
    return sorted(set(word1) ^ set(word2))

print(letters_in_either("apple", "pear"))
print(letters_in_both("apple", "pear"))
print(letters_in_one_only("apple", "pear"))
