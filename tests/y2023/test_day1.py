import pytest
from y2023.Day1.solution import solve_part1, solve_part2

@pytest.mark.parametrize("input_data, expected", [
    ("""1abc2
    pqr3stu8vwx
    a1b2c3d4e5f
    treb7uchet
    twothree6""", 208),
])
def test_solve_part1(input_data, expected):
    assert solve_part1(input_data) == expected

@pytest.mark.parametrize("input_data, expected", [
    ("""two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen""",281)
    # Part 2 test cases: ("input", "expected output"),
])
def test_solve_part2(input_data, expected):
    assert solve_part2(input_data) == expected
