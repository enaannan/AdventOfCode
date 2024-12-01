# Advent of Code 2024 - Day 1
def solve_part1(input_data):
    left =[]
    right=[]

    for pair in input_data.strip().split('\n'):
        (a,b) = map(int,pair.split())

        left.append(a)
        right.append(b)

    left.sort()
    right.sort()

    return sum(abs(left-right) for left,right in zip(left,right))

def solve_part2(input_data):
    left =[]
    right=[]
    for pair in input_data.split('\n'):
        (a,b) = map(int, pair.split())
        left.append(a)
        right.append(b)
    return sum(right.count(num)*num for num in left)
