

from functools import reduce
from utils import load_data

import string

priorities = {letter: prio for prio, letter in enumerate(string.ascii_lowercase + string.ascii_uppercase, start=1)} 

def split_compartments(input_line: str) -> tuple[str, str]:
    return input_line[:int(len(input_line)/2)], input_line[int(len(input_line)/2):]

def common_items(compartment_1, compartment_2):
    return set(compartment_1) & set(compartment_2)

def split_groups(lines: list[str], group_size=3):
    total_lines = len(lines)
    
    for start_of_group in range(0, total_lines, group_size):
        end_of_group = min(start_of_group + group_size, total_lines)
        yield lines[start_of_group: end_of_group]


def calc_part_1(data):
    total_priority = 0
    for line in data:
        compartment_1, compartment_2 = split_compartments(line)
        common = common_items(compartment_1, compartment_2)
        if len(common) != 1:
            raise ValueError()
        line_priority = priorities[common.pop()]
        total_priority += line_priority

    print(f"part 1 {total_priority}")
    
def calc_part_2(data):
    total_priority = 0
    for group in split_groups(data):
        common = set(group[0]) & set(group[1]) & set(group[2])
        if len(common) != 1:
            raise ValueError()
        line_priority = priorities[common.pop()]
        total_priority += line_priority
    print(f"part 2 {total_priority}")

day_data = load_data()
demo_data = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw""".splitlines()
calc_part_1(day_data)
calc_part_2(day_data)
