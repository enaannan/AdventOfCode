# Advent of Code 2023 - Day 2
import operator
import re
from collections import defaultdict
from functools import reduce

def solve_part1(data):
    default_values = {'red': 12, 'green': 13, 'blue': 14}
    sum = 0
    input_data=data.strip().split('\n')
    for index, game in enumerate(input_data, start=1):
        matches = re.findall(r'(\d+)\s*(red|green|blue)', game)
        if not any(int(num) > default_values[color] for num, color in matches):
            sum += index
    return sum

def solve_part2(data):
    sum_power_numbers = 0
    input_data = data.strip().split('\n')
    for game in input_data:
        matches = re.findall(r'(\d+)\s*(red|green|blue)', game)
        grouped_colors = defaultdict(list)
        for num, color in matches:
            grouped_colors[color].append(int(num))
        max_values = {color: max(numbers) for color, numbers in grouped_colors.items()}
        sum_power_numbers += reduce(operator.mul, max_values.values(), 1)
    return sum_power_numbers