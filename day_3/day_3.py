
input = "123456789"

for i, d in enumerate(input):
    print(i, d)

import itertools as it
combos = [x for x in it.product(range(2), repeat=3) if sum(x) == 12]

input = "234234234234278"

input = """987654321111111
811111111111119
234234234234278
818181911112111"""

with open("input.txt") as f:
    input_list = [line.rstrip() for line in f]

import itertools as it  
def get_max(input):
    max = 0
    for x in it.product(range(2), repeat=len(input)):
        if sum(x) == 12:
            candidate = int("".join(it.compress(input, x)))
            if candidate > max:
                max = candidate
    return max

def get_all_max(input):
    results = []
    for line in input:
        results.append(get_max(line))
    return results

results = get_all_max(input_list)
print(sum(results))

line = "234234234234278"
max_index, max = 0, 0

def find_max_index(line, size, start_index=0):
    max_index, max = 0, 0
    offset = len(line) - size - start_index + 1
    for i, d in enumerate(line[start_index:start_index+offset]):
        if int(d) > max:
            max = int(d)
            max_index = i
    return max_index + start_index

def find_max_number(line):
    indices = []
    max_index = -1
    for i in range(12, 0, -1):
        max_index = find_max_index(line, i, max_index+1)
        indices.append(max_index)
    return "".join([line[i] for i in indices])

def get_all_max(input):
    results = []
    for line in input:
        results.append(int(find_max_number(line)))
    return results

results = get_all_max(input_list)