from typing import List, IO
from functools import reduce


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
    return reduce(
        lambda acc, ele: (lambda: acc[-1].append(ele) if ele else acc.append([]))() or acc,
        [None if cal == "\n" else int(cal) for cal in file.readlines()],
        [[]]
    )


def part_one(calories: List[List[int]]):
    return reduce(
        lambda most, calorie_list: sum(calorie_list) if sum(calorie_list) > most else most,
        calories,
        0
    )

def part_two(calories: List[List[int]], top_elves=3):
    # needed due to the fact that we cannot do assignments in lambda expressions
    def _replace(calories: List[int], idx: int, sum_cal: int):
        calories[idx] = sum_cal

    '''
    pseudo-code explanation:

    stack = [0] * num_elves

    for each calorie_set : elf_calorie_sets:
        smallest_idx, smallest_amount = find_min(stack)

        if sum(calorie_set) > smallest_amount:
            stack[smallest_idx] = sum(calorie_set)

    return sum(stack)
    '''
    return sum(reduce(
        lambda acc, calorie_list:
            (lambda idx, sum_cal: _replace(acc, idx, sum_cal) or acc if idx >= 0 else acc)(
                (lambda res: res[0] if res[1] < sum(calorie_list) else -1)(
                    reduce(
                        lambda smallest, ele:
                            [smallest[0] + smallest[-1], ele, 0] if ele < smallest[1]
                            else smallest[:2] + [smallest[-1] + 1],
                        acc,
                        [0, acc[0], 0]
                    )
                ),
                sum(calorie_list)
            ),
        calories,
        [0]*top_elves
    ))


def main():
    with open("input.txt") as f:
        calories = parse_input(f)
        print("part 1 {}".format(part_one(calories=calories)))
        print("part 2 {}".format(part_two(calories=calories)))

main()
