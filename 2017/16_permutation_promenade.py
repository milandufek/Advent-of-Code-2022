from my_utils import get_data


# https://adventofcode.com/2017/day/16


def dance(moves: str, s: str = 'abcdefghijklmnop') -> str:
    for move in moves.split(','):
        if move[0] == 's':
            n = int(move[1:])
            s = s[-n:] + s[:-n]
        elif move[0] == 'x':
            a, b =  map(int, move[1:].split('/'))
            if a > b:
                a, b = b, a
            s = s[:a] + s[b] + s[a + 1:b] + s[a] + s[b + 1:]
        elif move[0] == 'p':
            a, b = move[1:].split('/')
            s = s.replace(a, 'x').replace(b, a).replace('x', b)
        else:
            raise ValueError(f'Invalid move: {move}')

    return s


def solve_2(moves: str) -> str:
    s = 'abcdefghijklmnop'
    n = 1_000_000_000
    seen = []
    for i in range(n):
        if s in seen:
            return seen[n % i]
        seen.append(s)
        s = dance(moves, s)

    return s


if __name__ == '__main__':
    data_input = get_data('inputs/16.in')[0]
    print(f'Part 1: {dance(data_input)}')
    print(f'Part 2: {solve_2(data_input)}')
