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

    sum = 0
    for r in ranges:
        str_numbers = generate_range_numbers_as_strings(r)
        for n in str_numbers:
            c_len = len(n)

            # only look at numbers divisable by 2
            if c_len % 2 != 0:
                continue

            split_at = int(c_len / 2)
            left = n[:split_at]
            right = n[split_at:]
  
            # exclude zero as a possible half
            if right == 0:
                continue

            if left == right:
                sum += int(n)

    return sum

def generate_range_numbers_as_strings(r):
    return list(map(str, range(r[0], r[1]+1)))

if __name__ == '__main__':
    file_path = sys.argv[1]
    ranges = parse_file(file_path)
    result_part1 = solve_part1(ranges)
    print(f"Part 1: {result_part1}, should be 1227775554")
