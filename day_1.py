import math

with open("day_1_input.txt") as f:
    input_list = [line.rstrip() for line in f]

def count_pointer_at_zero(input_list):
    pos = 50
    counter = 0
    for x in input_list:
        if x[0] == 'L':
            pos = pos - int(x[1:])
            if pos == 100:
                pos = 0
            if pos < 0:
                pos = pos % 100
        if x[0] == 'R':
            pos = pos + int(x[1:])
            if pos == 100:
                pos = 0
            if pos > 100:
                pos = pos % 100
        if pos == 0:
            counter = counter + 1
    return(counter)

def count_zero_crossings(input_list):      
    pos = 50
    counter = 0
    zero_count = 0
    for x in input_list:
        incr = int(x[1:])
        if x[0] == 'L':
            total_diff = pos - incr
            if total_diff <= 0:
                div_by_100 = abs(math.ceil(total_diff / 100))
                if pos == 0:
                    zero_count = div_by_100
                else:
                    zero_count = div_by_100 + 1
            else:
                zero_count = 0
            pos = (pos - incr) % 100
        if x[0] == 'R':
            total_diff = pos + incr
            if total_diff >= 100:
                div_by_100 = math.floor(total_diff/100)
                zero_count = div_by_100
            else:
                zero_count = 0
            pos = (pos + incr) % 100
        counter = counter + zero_count
    return(counter)

count_pointer_at_zero(input_list)
count_zero_crossings(input_list)