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

def solve_part2(pointer_start, operations):
    pointer = pointer_start
    zeroCounter = 0

    for operation in operations:
        direction = operation[:1]
        distance = int(operation[1:])
        sign = -1 if direction == 'L' else 1
        change = (distance * sign)

        quotient = (pointer + change) // 100
        new_pointer = (pointer + change) % 100

        # handle starting at 0 case for left rotation
        if pointer == 0 and quotient < 0:
            quotient += 1

        # handle ending at 0 case when going left
        if new_pointer == 0 and quotient <= 0:
            zeroCounter += 1

        zeroCounter += abs(quotient)
        pointer = new_pointer


    return zeroCounter

if __name__ == '__main__':
    file_path = sys.argv[1]
    operations = parse_file(file_path)
    result_part1 = solve_part1(50, operations)
    print(f"Part 1: {result_part1}, should be 3")
    result_part2 = solve_part2(50, operations)
    print(f"Part 2: {result_part2}, should be 6")
