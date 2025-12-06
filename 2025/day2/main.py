import sys

def parse_file(file_path):
    ranges = []
    with open(file_path) as file:
        for line in file:
            ranges_raw = line.split(",")
            
        for r in ranges_raw:
            ranges.append(list(map(int, r.split("-"))))
    return ranges 

def solve_part1(ranges):

    return 0

if __name__ == '__main__':
    file_path = sys.argv[1]
    ranges = parse_file(file_path)
    result_part1 = solve_part1(ranges)
    print(f"Part 1: {result_part1}, should be 1227775554")
