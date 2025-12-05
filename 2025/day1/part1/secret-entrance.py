import sys

# setup
input_filename = sys.argv[1]
pointer = 50
operations = []
with open(input_filename) as file:
    operations = [line.rstrip() for line in file]
zeroCounter = 0

# execute operations
for operation in operations:
    direction = operation[:1]
    distance = int(operation[1:])
    sign = -1 if direction == 'L' else 1
    pointer = (pointer + (distance * sign)) % 100
    if pointer == 0:
        zeroCounter += 1
  
# print result
print('Times hitting to zero:', zeroCounter)
