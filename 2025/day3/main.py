import sys

def parse_file(file_path):
    banks = []
    with open(file_path) as file:
        banks = [line.rstrip() for line in file]
    return banks

def solve_part1(banks):
    sum = 0
    digits = 2
    for bank in banks:
        result = find_largest_digits(bank, digits)
        sum += int(result)
    return sum

def solve_part2(banks):
    sum = 0
    digits = 12
    for bank in banks:
        result = find_largest_digits(bank, digits)
        sum += int(result)
    return sum

def find_largest_digits(bank, digits):
    if digits == 0:
        return ''

    current_max = 0
    current_max_index = 0
    for i in range(0, len(bank)-(digits-1)):
        n = int(bank[i])
        if n > current_max:
            current_max = n
            current_max_index = i

    return str(current_max) + find_largest_digits(bank[current_max_index+1:], digits-1)

if __name__ == '__main__':
    file_path = sys.argv[1]
    banks = parse_file(file_path)
    result_part1 = solve_part1(banks)
    print(f"Part 1: {result_part1}, should be 357")
    result_part2 = solve_part2(banks)
    print(f"Part 2: {result_part2}, should be 3121910778619") 
