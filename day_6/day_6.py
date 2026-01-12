input = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +"""

input = open("input.txt", "r").read()

input_array = [line.split() for line in  input.split("\n")]
rows = len(input_array)
cols = len(input_array[0])

ops = []
for c in range(cols):
    row_nums = []
    for r in range(rows-1):
        print(c, r)
        row_nums.append(int(input_array[r][c]))
    row = (input_array[rows-1][c], row_nums)
    ops.append(row)

import math

total = 0
for o in ops:
    if o[0] == "+":
        result = sum(o[1])
    if o[0] == "*":
        result = math.prod(o[1])
    total += result

def get_char(str, n):
    if n > len(str) - 1:
        return ""
    return str[n]

ops_transposed = []
for o in ops:
    max_digits = max([len(str(item)) for item in o[1]])
    nums_transposed = []
    for i in range(max_digits):
        num = ""
        for j in o[1]:
            num = num + get_char(str(j), i)
        nums_transposed.append(num)
    ops_transposed.append((o[0], nums_transposed))
        
ops = []
for c in range(cols):
    row_nums = []
    for r in range(rows-1):
        print(c, r)
        row_nums.append(input_array[r][c]))
    row = (input_array[rows-1][c], row_nums)
    ops.append(row)


# Part 2

input = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +"""

input = open("input.txt").read()
lines = input.split("\n")

import math
ops = lines[-1:][0].split()
rows = len(lines)
max_len = max(len(line) for line in lines)

start, end = 0, 0
ops_line = lines[-1:][0]
ranges = []
i = 1
for i in range(1, len(ops_line)):
    print(i)
    if ops_line[i] != " ":
        ranges.append([start, i])
        start = i

ranges.append([start, max_len+1])

input_transposed = []
for start, end in ranges:
    nums = []
    for r in range(rows - 1):
        if r < rows - 1:
            nums.append(lines[r][start:end-1])
        else:
            nums.append(lines[r][start:end])
    input_transposed.append(nums)

final_input = []
for row in input_transposed:
    max_len = max([len(item) for item in row])
    nums = []
    for i in range(max_len):
        num = ""
        for j in row:
            num = num + j[i]
        nums.append(int(num))
    final_input.append(nums)

total = 0
for i, op in enumerate(ops):
    print(op, final_input[i])
    if op == "+":
        total = total + sum([num for num in final_input[i]])
    if op == "*":
        total = total + math.prod([num for num in final_input[i]])
    