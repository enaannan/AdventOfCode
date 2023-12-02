from y2023.Day1.solution import solve_part2, solve_part1

if __name__ == '__main__':
    with open('E:/me/projects/Kata/Python/AdventOfCode/y2023/Day1/input.txt', 'r') as file:
        input_data = file.read()

    test="""
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
    """
    formatted_input = input_data.strip().split('\n')
    # formatted_input = test.strip().split('\n')

    print(solve_part1(input_data))