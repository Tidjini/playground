"""Generate EAN 13 Barre Code using:

random and randrange
"""

from random import randrange
from functools import reduce


def generate(length: int = 12) -> list:
    """Generate n (length) random number

    in EAN 13 must generate 12 numbers from 2-9
    """
    numbers = []
    for n in range(length):
        numbers.append(randrange(2, 10))
    return numbers


def checksum(numbers: list) -> int:
    """EAN 13 checksum"""

    def sum(x, y):
        return int(x) + int(y)

    evensum = reduce(sum, numbers[::2])
    oddsum = reduce(sum, numbers[1::2])

    return (10 - ((evensum + oddsum * 3) % 10)) % 10


def generate_ean_13() -> str:
    """Return Generated EAN 13"""
    digits = generate()
    digits.append(checksum(digits))
    return "".join(map(str, digits))
