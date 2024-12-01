import pytest
from y2024.Day1.solution import solve_part1, solve_part2

# Read input from file
with open("../y2024/Day1/input.txt", 'r') as file:
    file_contents = file.read()

@pytest.mark.parametrize("input_data, expected", [
("""3   4
4   3
2   5
1   3
3   9
3   3""",11),(file_contents,2742123)
])
def test_solve_part1(input_data, expected):
    assert solve_part1(input_data) == expected

@pytest.mark.parametrize("input_data, expected", [
("""3   4
4   3
2   5
1   3
3   9
3   3""",31),(file_contents,21328497)
])
def test_solve_part2(input_data, expected):
    assert solve_part2(input_data) == expected
