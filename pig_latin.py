vowels = "aeiouy"


def pig_latin(word):
    """Pig Latin:

    if first letter of word is constant then move it to end with additional 'ay'.
    else concat 'way' with this word, ex: pig -> igpay | Eric -> Ericway
    """

    if word[0].lower() not in vowels:
        return "{}{}ay".format(word[1:], word[0].lower())

    return word + "way"


if __name__ == "__main__":

    pig_word = pig_latin("Eric")
    print(pig_word)
