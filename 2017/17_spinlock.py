from collections import deque
from my_utils import get_data


# https://adventofcode.com/2017/day/17


def solve_1(num: int, cycles: int) -> int:
    buffer = deque([0])
    for i in range(1, cycles + 1):
        buffer.rotate(-num)
        buffer.append(i)

    return buffer[0]


def solve_2(num: int, cycles: int) -> int:
    position = 0
    result = 0
    for i in range(1, cycles + 1):
        position = (position + num) % i + 1
        if position == 1:
            result = i

    return result


if __name__ == '__main__':
    data_input = int(get_data('inputs/17.in')[0].strip())
    print(f'Part 1: {solve_1(data_input, cycles=2017)}')
    print(f'Part 2: {solve_2(data_input, cycles=50_000_000)}')
