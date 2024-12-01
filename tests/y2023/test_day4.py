import pytest
from y2023.Day4.solution import solve_part1, solve_part2

@pytest.mark.parametrize("input_data, expected", [
    # Part 1 test cases: ("input", "expected output"),
])
def test_solve_part1(input_data, expected):
    assert solve_part1(input_data) == expected

@pytest.mark.parametrize("input_data, expected", [
    # Part 2 test cases: ("input", "expected output"),
])
def test_solve_part2(input_data, expected):
    assert solve_part2(input_data) == expected
