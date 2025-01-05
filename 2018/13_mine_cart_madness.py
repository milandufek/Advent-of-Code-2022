from dataclasses import dataclass
from my_utils import get_data


# https://adventofcode.com/2018/day/13


@dataclass
class Cart:
    r: int
    c: int
    dir: str
    turns: int = 0
    crashed: bool = False


def parse_input(data: list[str]) -> tuple[list[list[str]], list[Cart]]:
    grid: list[list[str]] = []
    carts: list[Cart] = []
    rows = len(data)
    cols = len(data[0])
    for r in range(rows):
        grid.append([])
        for c in range(cols):
            char = data[r][c]
            if char in ('v', '^', '<', '>'):
                carts.append(Cart(c, r, char))
                if char in ('v', '^'):
                    grid[r].append('|')
                else:
                    grid[r].append('-')
            else:
                grid[r].append(char)
    return grid, carts


def print_grid(grid: list[list[str]], carts: list[Cart]) -> None:
    grid = [row.copy() for row in grid]
    for cart in carts:
        grid[cart.c][cart.r] = cart.dir
    for row in grid:
        print(''.join(row))
    print()


def solve_1(data: list[str]) -> str:
    grid, carts = parse_input(data)
    dir_map = {'>': (1, 0), 'v': (0, 1), '<': (-1, 0), '^': (0, -1)}
    turn_left = lambda dir: '>v<^'[('>v<^'.index(dir) - 1) % 4]
    turn_right = lambda dir: '>v<^'[('>v<^'.index(dir) + 1) % 4]
    while True:
        # print_grid(grid, carts)
        for cart in carts:
            dr, dc = dir_map[cart.dir]
            cart.r += dr
            cart.c += dc

            for other_cart in carts:
                if cart != other_cart and cart.r == other_cart.r and cart.c == other_cart.c:
                    return f'{cart.r},{cart.c}'

            if grid[cart.c][cart.r] == '+':
                if cart.turns == 0:
                    cart.dir = turn_left(cart.dir)
                elif cart.turns == 2:
                    cart.dir = turn_right(cart.dir)
                cart.turns = (cart.turns + 1) % 3
            elif grid[cart.c][cart.r] == '\\':
                if cart.dir in ('>', '<'):
                    cart.dir = turn_right(cart.dir)
                else:
                    cart.dir = turn_left(cart.dir)
            elif grid[cart.c][cart.r] == '/':
                if cart.dir in ('>', '<'):
                    cart.dir = turn_left(cart.dir)
                else:
                    cart.dir = turn_right(cart.dir)
            elif grid[cart.c][cart.r] not in '|-':
                raise ValueError(f'Invalid grid char: {grid[cart.c][cart.r]}')


def solve_2(data: list[str]) -> str:
    grid, carts = parse_input(data)
    dir_map = {'>': (1, 0), 'v': (0, 1), '<': (-1, 0), '^': (0, -1)}
    turn_left = lambda dir: '>v<^'[('>v<^'.index(dir) - 1) % 4]
    turn_right = lambda dir: '>v<^'[('>v<^'.index(dir) + 1) % 4]
    while True:
        carts = [cart for cart in carts if not cart.crashed]
        carts.sort(key=lambda cart: (cart.c, cart.r))

        if len(carts) == 1:
            return f'{carts[0].r},{carts[0].c}'

        for cart in carts:
            dr, dc = dir_map[cart.dir]
            cart.r += dr
            cart.c += dc

            for other_cart in carts:
                if cart != other_cart and cart.r == other_cart.r and cart.c == other_cart.c:
                    cart.crashed = True
                    other_cart.crashed = True

            if cart.crashed:
                continue

            if grid[cart.c][cart.r] == '+':
                if cart.turns == 0:
                    cart.dir = turn_left(cart.dir)
                elif cart.turns == 2:
                    cart.dir = turn_right(cart.dir)
                cart.turns = (cart.turns + 1) % 3
            elif grid[cart.c][cart.r] == '\\':
                if cart.dir in ('>', '<'):
                    cart.dir = turn_right(cart.dir)
                else:
                    cart.dir = turn_left(cart.dir)
            elif grid[cart.c][cart.r] == '/':
                if cart.dir in ('>', '<'):
                    cart.dir = turn_left(cart.dir)
                else:
                    cart.dir = turn_right(cart.dir)
            elif grid[cart.c][cart.r] not in '|-':
                raise ValueError(f'Invalid grid char: {grid[cart.c][cart.r]}')


if __name__ == '__main__':
    # data_input = get_data('inputs/13_example.in')
    data_input = get_data('inputs/13.in')
    print(f'Part 1: {solve_1(data_input)}')
    # data_input = get_data('inputs/13_example2.in')
    print(f'Part 2: {solve_2(data_input)}')
