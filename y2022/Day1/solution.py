# Advent of Code 2020 - Day 1
def solve(input_data):
    # Split the input data into groups separated by blank lines
    elf_groups = input_data.strip().split('\n\n')

    # Calculate the total calories for each Elf
    max_calories = 0
    for group in elf_groups:
        # Sum up the calories for each Elf
        calories = sum(int(item) for item in group.splitlines())
        # Update the maximum calories if this Elf has more
        max_calories = max(max_calories, calories)

    return max_calories
