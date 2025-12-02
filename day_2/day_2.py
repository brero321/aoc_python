
# Day 2: Part 1

def get_invalid_ids(input_list):
    invalid_ids = []
    for rng in input_list:
        start, end = map(int, rng.split("-"))
        for n in range(start, end + 1):
            str_n = str(n)
            n_chars = len(str_n)
            if n_chars % 2 == 0:
                midpoint = int(n_chars / 2)
                if str_n[0:midpoint] == str_n[midpoint:]:
                    invalid_ids.append(n)
    return invalid_ids

input = "503950-597501,73731-100184,79705998-79873916,2927-3723,35155-50130,52-82,1139-1671,4338572-4506716,1991-2782,1314489-1387708,8810810-8984381,762581-829383,214957-358445,9947038-10058264,4848455367-4848568745,615004-637022,5827946-5911222,840544-1026063,19-46,372804-419902,486-681,815-1117,3928-5400,28219352-28336512,6200009-6404247,174-261,151131150-151188124,19323-26217,429923-458519,5151467682-5151580012,9354640427-9354772901,262-475,100251-151187,5407-9794,8484808500-8484902312,86-129,2-18"
input_example = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
input_list = input.split(",")

sum(get_invalid_ids(input_list))

# Day 2: Part 2

import math    
def get_factors(n):
    factors = []
    for i in range(1, math.floor(n / 2) + 1):
        if n % i == 0:
            factors.append(i)
        if len(factors) > 1 and 1 in factors:
            factors.remove(1)
    return(factors)

def check_number(n):
    invalid_id = False
    str_n = str(n)
    n_chars = len(str_n)
    factors = get_factors(n_chars)
    for d in factors:
        seg_val = set()
        for i in range(int(n_chars / d)):
            seg_val.add(str_n[i*d:(i+1)*d])
        if len(seg_val) == 1:
            invalid_id = True
    return(invalid_id)

def get_invalid_ids(input_list):
    invalid_ids = set()
    for rng in input_list:
        start, end = map(int, rng.split("-"))
        for n in range(start, end + 1):
            if check_number(n) == True:
                invalid_ids.add(n)
    return invalid_ids


input_example = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
input_list = input_example.split(",")

input = "503950-597501,73731-100184,79705998-79873916,2927-3723,35155-50130,52-82,1139-1671,4338572-4506716,1991-2782,1314489-1387708,8810810-8984381,762581-829383,214957-358445,9947038-10058264,4848455367-4848568745,615004-637022,5827946-5911222,840544-1026063,19-46,372804-419902,486-681,815-1117,3928-5400,28219352-28336512,6200009-6404247,174-261,151131150-151188124,19323-26217,429923-458519,5151467682-5151580012,9354640427-9354772901,262-475,100251-151187,5407-9794,8484808500-8484902312,86-129,2-18"
input_list = input.split(",")

sum(get_invalid_ids(input_list))