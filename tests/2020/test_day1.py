import pytest
from y2022.Day1.solution import solve


@pytest.mark.parametrize("input_data, expected", [
    ("""
     1000
     2000
     3000

     4000

     5000
     6000

     7000
     8000
     9000

     10000
     """, 24000),
])

def test_solve(input_data, expected):
    assert solve(input_data) == expected
