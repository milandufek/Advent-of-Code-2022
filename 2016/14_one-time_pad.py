import re
from functools import cache
from hashlib import md5
from typing import Generator, Any, Match
from my_utils import get_data


# https://adventofcode.com/2016/day/14


three_in_row = re.compile(r'(.)\1\1')


@cache
def get_hash(salt: str, stretch: int = 0) -> str:
    md5_hash = salt
    for _ in range(stretch + 1):
        md5_hash = md5(md5_hash.encode()).hexdigest()
    return md5_hash


def find_three_in_row(salt: str, stretch: int = 0) -> str:
    return three_in_row.search(get_hash(salt, stretch))


def is_valid_key(index: int, char: str, salt: str, stretch: int = 0) -> bool:
    for i in range(1000):
        if char * 5 in get_hash(f'{salt}{index + i + 1}', stretch):
            return True
    return False


def generate_key(salt: str, stretch: int = 0) -> Generator[int, Any, None]:
    for index in range(1_000_000_000):
        match: Match[str]
        if match := find_three_in_row(f'{salt}{index}', stretch):
            if is_valid_key(index, match.group(1), salt, stretch):
                yield index
    yield -1


def solve_1(salt: str) -> int:
    generated_key = generate_key(salt)
    for _ in range(64):
        key = next(generated_key)
    return key


def solve_2(salt: str) -> int:
    generated = generate_key(salt, 2016)
    for _ in range(64):
        key = next(generated)
    return key


if __name__ == '__main__':
    data_input = get_data('inputs/14.in')[0].strip()
    print(f'Part 1: {solve_1(data_input)}')
    print(f'Part 2: {solve_2(data_input)}')
