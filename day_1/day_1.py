import math

with open("day_1_input.txt") as f:
    input_list = [line.rstrip() for line in f]

def count_pointer_at_zero(input_list):
    pos = 50
    counter = 0
    input_list = [(-1 if x[0] == 'L' else 1) * int(x[1:]) for x in input_list]
    for x in input_list:
        pos = pos + x
        pos = pos % 100
        if pos == 0:
            counter = counter + 1
    return(counter)

def count_zero_crossings(input_list):      
    pos = 50
    counter = 0
    zero_count = 0
    input_list = [(-1 if x[0] == 'L' else 1) * int(x[1:]) for x in input_list]
    for x in input_list:
        total_diff = pos + x
        if total_diff <= 0:
            div_by_100 = abs(math.ceil(total_diff / 100))
            if pos == 0:
                zero_count = div_by_100
            else:
                zero_count = div_by_100 + 1
        elif total_diff >= 100:
                div_by_100 = math.floor(total_diff/100)
                zero_count = div_by_100
        else:
            zero_count = 0
        pos = (pos + x) % 100
        counter = counter + zero_count
    return(counter)