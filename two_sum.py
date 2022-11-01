sample = [1, -1, 5, 5, 10, 2, 80]
sample_sorted = sorted(sample)

target = 10


class Solution:
    @classmethod
    def brute(cls, array, sum):

        for i in range(len(array)):
            for j in range(i + 1, len(array)):
                if array[i] + array[j] == sum:
                    return (i + 1, j + 1)

        raise ValueError("this sum not exist")

    @classmethod
    def hashing(cls, array, sum):

        hasher = {}
        for index, value in enumerate(array):
            if sum - value in hasher:
                return (hasher[sum - value] + 1, index + 1)

            hasher[value] = index

        raise ValueError("this sum not exist")

    @classmethod
    def left_right(cls, array, sum):
        left = 0
        right = len(array) - 1

        while left < right:
            s = array[left] + array[right]

            if s > sum:
                right -= 1
            elif s < sum:
                left += 1
            else:
                return (left + 1, right + 1)

        raise ValueError("this sum not exist")

    # @classmethod
    # def bsearch(cls, array, left, sum):
    #     left = left
    #     right = len(array) - 1

    #     while left < right:
    #         midle = (left + right) // 2

    #         if sum - array[midle]
