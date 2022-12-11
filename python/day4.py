import re
from utils import load_data

demo_data = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""

real_data = load_data(split_lines=False)
    
def part_1(data):
    fully_overlapping_count = 0
    pattern = r"(?P<start1>\d+)-(?P<end1>\d+),(?P<start2>\d+)-(?P<end2>\d+)"
    for match in re.finditer(pattern=pattern, string=data):
        start1 = int(match.group("start1"))
        end1 = int(match.group("end1"))
        start2 = int(match.group("start2"))
        end2 = int(match.group("end2"))

        # n1 has a lower start
        if (start1 <= start2 and end2 <= end1) or (start2 <= start1 and end1 <= end2):
            fully_overlapping_count += 1

    print(f"{fully_overlapping_count=}")        

def part_2(data):
    overlapping_count = 0
    pattern = r"(?P<start1>\d+)-(?P<end1>\d+),(?P<start2>\d+)-(?P<end2>\d+)"
    for match in re.finditer(pattern=pattern, string=data):
        start1 = int(match.group("start1"))
        end1 = int(match.group("end1"))
        start2 = int(match.group("start2"))
        end2 = int(match.group("end2"))

        if (start1 <= start2 <= end1) or (start2 <= start1 <= end2):
            overlapping_count += 1

    print(f"{overlapping_count=}")        

part_1(real_data)
part_2(real_data)
