# https://adventofcode.com/2020/day/6


ANSWERS = 'abcdefghijklmnopqrstuvwxyz'


def get_data(file_path: str) -> str:
    with open(file_path) as f:
        return f.read()


def solve_1(data: str) -> int:
    return sum(
        1 for group in data.split('\n\n')
        for answer in ANSWERS if answer in group
    )


def solve_2(data: str) -> int:
    groups = list(map(lambda x: x.split('\n'), data.split('\n\n')))
    return sum(
        1 for group in groups
        for answer in ANSWERS
        if all(answer in person for person in group)
    )


if __name__ == '__main__':
    data_input = get_data('inputs/06.txt')
    print(f'#1: {solve_1(data_input)}')
    print(f'#2: {solve_2(data_input)}')
