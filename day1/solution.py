from typing import List, IO
import functools


test_input = '''1000
2000
3000

4000

5000
6000

7000
8000
9000

10000'''

def parse_input(file: IO) -> List[List[int]]:
    return functools.reduce(
        lambda acc, ele: (lambda: acc[-1].append(ele) if ele else acc.append([]))() or acc,
        [None if cal == "\n" else int(cal) for cal in file.readlines()],
        [[]]
    )


def part_one(calories: List[List[int]]):
    return functools.reduce(
        lambda most, calorie_list: sum(calorie_list) if sum(calorie_list) > most else most,
        calories,
        0
    )

def part_two(calories: List[List[int]], top_elves=3):
    def _find_idx(calories: List[int], sum_cal: int) -> int:
        smallest = calories[0]
        i = 0
        for idx, c in enumerate(calories):
            if c < smallest:
                i = idx
                smallest = c
        return i if sum_cal > smallest else -1

    def _replace(calories: List[int], sum_cal: int):
        idx = _find_idx(calories, sum_cal)
        if idx >= 0:
            calories[idx] = sum_cal

        return calories

    return sum(functools.reduce(
        lambda acc, calorie_list: _replace(acc, sum(calorie_list)),
        calories,
        [0]*top_elves
    ))


def main():
    with open("input.txt") as f:
        calories = parse_input(f)
        print("part 1 {}".format(part_one(calories=calories)))
        print("part 2 {}".format(part_two(calories=calories)))

main()
