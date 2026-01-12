
input = """.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
..............."""

input = open("input.txt", "r").read()

input_list = input.split("\n")
input_items = []
for item in input_list:
    line = [ch for ch in item]
    input_items.append(line)

max_col = len(input_items[0])
start_col = 70

positions = set([70])
counter = 0
for i in range(1, len(input_list)-1):
    next_positions = set()
    for p in positions:
        if input_items[i][p] == ".":
            next_positions.add(p)
        if input_items[i][p] == "^":
            counter = counter + 1
            if p - 1 >= 0:
                next_positions.add(p - 1)
            if p + 1 < max_col:
                next_positions.add(p + 1)
    positions = next_positions
    print(next_positions, "counter:", counter)

# Part 2

input = """.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
..............."""

input = open("input.txt", "r").read()

input_list = input.split("\n")
input_items = []
for item in input_list:
    line = [ch for ch in item]
    input_items.append(line)

positions = {7: 1}
max_col = len(input_list[0])
for i in range(1, len(input_list)-1):
    next_positions = {}
    for p, v in positions.items():
        if input_items[i][p] == ".":
            next_positions[p] = next_positions.get(p, 0) + v
        if input_items[i][p] == "^":
            if p - 1 >= 0:
                next_positions[p - 1] = next_positions.get(p - 1, 0) + v
            if p + 1 < max_col:
                next_positions[p + 1] = next_positions.get(p + 1, 0) + v
    positions = next_positions
    print(next_positions)

sum(positions.values())