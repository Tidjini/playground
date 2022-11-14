def poor_man_bar_chart(sentence):
    """Set Chart of letters

    for each letter in sentence add it to a list
    """

    results = {}

    for letter in sentence:
        if letter not in results:
            results[letter] = [letter]
            continue
        results[letter].append(letter)
