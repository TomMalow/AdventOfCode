import sys

def parse_file(file_path):
    rows = []
    with open(file_path) as file:
        rows = [line.rstrip() for line in file]
    return (rows)

def solve_part1(rows):
    return 0

def solve_part2(rows):
    return 0

if __name__ == '__main__':
    file_path = sys.argv[1]
    data = parse_file(file_path)
    result_part1 = solve_part1(data)
    print(f"Part 1: {result_part1}, should be 13")
    result_part2 = solve_part2(data)
    print(f"Part 2: {result_part2}, should be ??") 
