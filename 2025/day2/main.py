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

def solve_part2(ranges):

    divisors_cache = {}
    sum = 0
    for r in ranges:
        str_numbers = generate_range_numbers_as_strings(r)
        matches = []
        for n in str_numbers:
            c_len = len(n)

            # get all divisors of c_len excluding c_len itself
            divisors = divisors_cache.get(c_len)
            if divisors is None:
                divisors = generate_divisors(c_len) 
                divisors_cache[c_len] = divisors    

            # generate all sub strings based on divisors
            generated_substrings = generate_substrings(n, divisors)

            for parts in generated_substrings:

                if check_sub_parts(parts):
                    matches.append(n)
                    sum += int(n)
                    break 

    return sum

def check_sub_parts(parts):
    first = parts[0]
    for part in parts:
        if first != part:
            return False
            break
    return True

def generate_substrings(n, divisors):
    potential_parts = []
    for d in divisors:
        parts = []
        for i in range(0, len(n), d):
            parts.append(n[i:i+d])
        potential_parts.append(parts)
    return potential_parts

def generate_divisors(n):
    divisors = []
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)
    return divisors
    
def generate_range_numbers_as_strings(r):
    return list(map(str, range(r[0], r[1]+1)))

if __name__ == '__main__':
    file_path = sys.argv[1]
    ranges = parse_file(file_path)
    result_part1 = solve_part1(ranges)
    print(f"Part 1: {result_part1}, should be 1227775554")
    result_part2 = solve_part2(ranges)
    print(f"Part 2: {result_part2}, should be 4174379265")
