# Advent of Code 2023 - Day 1
import re


def solve_part1(input_data):
    res=[]
    formatted_data = input_data.strip().split('\n')
    for line in formatted_data :
        digits = [char for char in line if char.isdigit()]
        res.append(int(digits[0]+digits[-1]))
        sum(res)
    return sum(res)

def solve_part2(input_data):
    res=[]
    line_numbers=[]
    formatted_data = input_data.strip().split('\n')
    for line in formatted_data:
        for char_index,char in enumerate(line):
            if(char.isdigit()):
                line_numbers.append(char)
            for mapping_index,value in enumerate(["one","two","three","four","five","six","seven","eight","nine"],start=1):
                if line[char_index:].startswith(value):
                    line_numbers.append(str(mapping_index))

        res.append(int(line_numbers[0]+line_numbers[-1]))
        line_numbers=[]
    return sum(res)
