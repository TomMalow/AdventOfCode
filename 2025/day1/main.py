import sys

def parse_file(file_path):
    operations = []
    with open(file_path) as file:
        operations = [line.rstrip() for line in file]
    return operations

def solve_part1(pointer_start, operations):
    pointer = pointer_start
    zeroCounter = 0

    for operation in operations:
        direction = operation[:1]
        distance = int(operation[1:])
        sign = -1 if direction == 'L' else 1
        pointer = (pointer + (distance * sign)) % 100

        if pointer == 0:
            zeroCounter += 1

    return zeroCounter

if __name__ == '__main__':
    file_path = sys.argv[1]
    operations = parse_file(file_path)
    result_part1 = solve_part1(50, operations)
    print(f"Part 1: {result_part1}, should be 3")
