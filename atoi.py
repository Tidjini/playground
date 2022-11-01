class Solution:
    @classmethod
    def atoi(cls, chaine):
        i = 0
        n = len(chaine)

        while i < n and chaine[i].isspace():
            i += 1

        sign = 1
        if chaine[i] == "+":
            i += 1
        if chaine[i] == "-":
            i += 1
            sign = -1
        ret = ""
        while i < n and chaine[i].isdigit():
            ret += chaine[i]
            i += 1

        return sign * int(ret) if ret != "" else 0
