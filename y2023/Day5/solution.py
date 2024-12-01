# Advent of Code 2023 - Day 5
def solve_part1(input_data):
    formatted_data_sections = input_data.strip().split('\n\n')

    sections_integers = []

    # Process each section
    for section in formatted_data_sections:
        lines = section.split(":")[1]

        lines = lines.strip().split('\n')

        section_integers = []

        for line in lines:
            section_integers.extend([int(num) for num in line.split()])

        sections_integers.append(section_integers)
    # seeds = [int(num) for num in formatted_data[0].split(":")[1].strip().split(" ")]
    # print
    # print(seeds)
    return None

def solve_part2(input_data):
    # Your solution for Part 2 goes here
    return None
