# Advent of Code 2024 - Day 1
def solve_part1(input_data):
    input_list = input_data.split('\n')
    left =[]
    right=[]
    for pair in input_list:
        (a,b) = pair.split()
        left.append(int(a))
        right.append(int(b))
    left.sort()
    right.sort()

    diff=[abs(left-right) for left,right in zip(left,right)]
    return sum(diff)

def solve_part2(input_data):
    input_list = input_data.split('\n')
    left =[]
    right=[]
    for pair in input_list:
        (a,b) = pair.split()
        left.append(int(a))
        right.append(int(b))
    multiple = [right.count(num)*num for num in left]
    return sum(multiple)
