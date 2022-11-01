target = "the sky is bule is sky the"  # return 'blue is sky the'


class Solution:
    @classmethod
    def revrese_pythonic(cls, target):
        words = target.split()
        left = 0
        right = len(words) - 1
        while left < right:
            words[right], words[left] = words[left], words[right]
            left += 1
            right -= 1

        return " ".join(words)

    @classmethod
    def double_reverse(cls, target):

        reverse = target[::-1]
        reversed_word = reverse.split()

        for index, word in enumerate(reversed_word):
            reversed_word[index] = word[::-1]

        return " ".join(reversed_word)
