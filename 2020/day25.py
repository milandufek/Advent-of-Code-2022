# https://adventofcode.com/2020/day/25


def get_data(file_path: str) -> list[str]:
    with open(file_path) as f:
        return f.readlines()


def solve(data: list[str]) -> int:
    ec, pub = map(int, data)
    subject_number = 7
    mod = 20201227
    value = 1
    loop_size = 0

    while value != ec:
        value *= subject_number
        value %= mod
        loop_size += 1

    return pow(pub, loop_size, mod)


if __name__ == '__main__':
    data_input = get_data('inputs/25.txt')
    print(f'{solve(data_input)}')
