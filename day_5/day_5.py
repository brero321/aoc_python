
input = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""

ranges = input.split("\n\n")[0].split("\n")
ingredients = input.split("\n\n")[1].split("\n")

def check_in_range(num, range_str):
    start, end = map(int, range_str.split("-"))
    return start <= num <= end

def check_in_all_ranges(num, range_str_list):
    for range_str in range_str_list:
        if check_in_range(num, range_str) == True:
            return True
    return False

def check_all_nums(input):
    ranges = input.split("\n\n")[0].split("\n")
    ingredients = map(int, input.split("\n\n")[1].split("\n"))
    return sum([check_in_all_ranges(num, ranges) for num in ingredients])

check_all_nums(input)

input = open("input.txt").read()

def get_total_unique_nums(input):
    ranges_sorted = sorted([list(map(int, r.split("-"))) for r in input.split("\n\n")[0].split("\n")], key = lambda x: x[0])
    total, prev_end = 0, 0
    for start, end in ranges_sorted:
        if prev_end >= start:
            start = prev_end + 1
        if prev_end >= end:
            diff = 0
        else:
            diff = end - start + 1
            prev_end = end
        total += diff
    return total

get_total_unique_nums(input)
