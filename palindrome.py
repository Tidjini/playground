from sqlalchemy import false, true


target = "A man, a plan, a canal: Panama"  # this, return ture


class Solution:
    @classmethod
    def use_pointers(cls, target):

        left = 0
        right = len(target) - 1

        while left < right:

            if not target[left].isalnum():
                left += 1
                continue
            if not target[right].isalnum():
                right -= 1
                continue

            if target[left].lower() != target[right].lower():
                return False

            left += 1
            right -= 1
        return True

    @classmethod
    def use_reverse(cls, target):
        other = []
        for n in target:
            if n.isalnum():
                other.append(n.lower())

        return other == other[::-1]
