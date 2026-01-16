def frequency_analysis(message):
    counts = {}

    for char in message.lower():
        if char.isalpha():
            counts[char] = counts.get(char, 0) + 1

    most_common = sorted(counts.items(), key=lambda x: x[1], reverse=True)[:6]

    for letter, count in most_common:
        print(letter, count)

frequency_analysis("This is an example of encrypted text")
