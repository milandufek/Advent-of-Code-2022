# https://adventofcode.com/2020/day/10


def get_data(file_path: str) -> list[str]:
    with open(file_path) as f:
        return f.readlines()


def solve_1(data: list[str]) -> int:
    jolts = [0] + sorted(map(int, data))
    diffs = [jolts[i + 1] - jolts[i] for i in range(len(jolts) - 1)]
    return diffs.count(1) * (diffs.count(3) + 1)


def solve_2(data: list[str]) -> int:
    jolts = [0] + sorted(map(int, data))
    jolts.append(jolts[-1] + 3)
    dp = [0] * len(jolts)
    dp[0] = 1

    for i in range(1, len(jolts)):
        for j in range(i):
            if jolts[i] - jolts[j] <= 3:
                dp[i] += dp[j]

    return dp[-1]


if __name__ == '__main__':
    # data_input = get_data('inputs/test.txt')
    data_input = get_data('inputs/10.txt')
    print(f'#1: {solve_1(data_input)}')
    print(f'#2: {solve_2(data_input)}')
