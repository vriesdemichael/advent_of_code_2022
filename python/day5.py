from utils import load_data
import re


real_data = load_data(split_lines=False)
demo_data = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""


def parse_instructions(raw_instructions: str):
    pattern = r"move (?P<amount> \d+) from (?P<from>\d+) to (?P<to>)))"
    yield re.finditer()

def split_input(data: str):
    start_state, instructions = data.split("\n\n")
    return start_state, instructions
    
print(split_input(demo_data))