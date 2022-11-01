"""needle in haystack

    Just Implementation
"""


class Solution:
    @classmethod
    def str_str(cls, haystack: str, needle: str):
        i = 0
        j = 0
        while True:
            while True:
                if j == len(needle):
                    return i
                if i + j == len(haystack):
                    return -1
                if needle[j] != haystack[i + j]:
                    break
