from itertools import batched


# https://adventofcode.com/2016/day/16


def dragon_curve(a: str) -> str:
    b = a[::-1]
    b = b.replace('0', 'x').replace('1', '0').replace('x', '1')
    return a + '0' + b


def checksum(s: str) -> str:
    check_sum = []
    for pair in batched(s, n=2):
        if len(pair) == 1:
            check_sum.append(pair[0])
            break

        check_sum.append('1' if pair[0] == pair[1] else '0')

    if len(check_sum) % 2 == 0:
        return checksum(''.join(check_sum))

    return ''.join(check_sum)


def solve(s: str, max_length: int) -> str:
    while len(s) < max_length:
        s = dragon_curve(s)

    return checksum(s[:max_length])


def test_dragon_curve():
    assert dragon_curve('1') == '100'
    assert dragon_curve('0') == '001'
    assert dragon_curve('11111') == '11111000000'
    assert dragon_curve('111100001010') == '1111000010100101011110000'


def test_checksum():
    assert checksum('110010110100') == '100'


def test_solve_1():
    assert solve('10000', max_length=20) == '01100'


if __name__ == '__main__':
    data_input = '10111100110001111'
    print(f'Part 1: {solve(data_input, max_length=272)}')
    print(f'Part 2: {solve(data_input, max_length=35651584)}')
