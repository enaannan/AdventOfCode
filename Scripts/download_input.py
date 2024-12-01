import requests
import argparse
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

def create_init_py(directory):
    init_py_path = os.path.join(directory, '__init__.py')
    if not os.path.exists(init_py_path):
        open(init_py_path, 'w').close()

def create_structure(year, day):
    year_dir = f'../y{str(year)}'
    if not os.path.exists(year_dir):
        os.makedirs(year_dir)
        create_init_py(year_dir)

    day_dir = os.path.join(year_dir, f"Day{day}")
    if not os.path.exists(day_dir):
        os.makedirs(day_dir)
        create_init_py(day_dir)

    solution_file_path = os.path.join(day_dir, 'solution.py')
    if not os.path.exists(solution_file_path):
        with open(solution_file_path, 'w') as solution_file:
            solution_file.write(f'''# Advent of Code {year} - Day {day}
def solve_part1(input_data):
    # Your solution for Part 1 goes here
    return None

def solve_part2(input_data):
    # Your solution for Part 2 goes here
    return None
''')

    tests_year_dir = f'../tests/y{str(year)}'
    if not os.path.exists(tests_year_dir):
        os.makedirs(tests_year_dir)
        create_init_py(tests_year_dir)

    test_file_path = os.path.join(tests_year_dir, f'test_day{day}.py')
    if not os.path.exists(test_file_path):
        with open(test_file_path, 'w') as test_file:
            test_file.write(f'''import pytest
            from y{year}.Day{day}.solution import solve_part1, solve_part2

            # Read input from file
            def read_input():
                with open("../y{year}/Day{day}/input.txt", 'r') as file:
                    return file.read()

            @pytest.mark.parametrize("input_data, expected", [
                (read_input(), None)  # Replace None with the expected result for Part 1
            ])
            def test_solve_part1(input_data, expected):
                assert solve_part1(input_data) == expected

            @pytest.mark.parametrize("input_data, expected", [
                (read_input(), None)  # Replace None with the expected result for Part 2
            ])
            def test_solve_part2(input_data, expected):
                assert solve_part2(input_data) == expected
            ''')

    return day_dir

def download_input(day, year):
    session_cookie = os.getenv('AOC_SESSION')
    if not session_cookie:
        raise ValueError("Session cookie not found. Please set AOC_SESSION in your .env file.")

    year_dir = f'../y{str(year)}'
    day_dir = os.path.join(year_dir, f"Day{day}")

    input_file_path = os.path.join(day_dir, 'input.txt')

    if os.path.exists(input_file_path) and os.path.getsize(input_file_path) > 0:
        print(f"Input file for year {year}, day {day} already exists and is not empty. Skipping download.")
        return

    url = f'https://adventofcode.com/{year}/day/{day}/input'
    cookies = {'session': session_cookie}
    response = requests.get(url, cookies=cookies)

    if response.status_code == 200:
        with open(input_file_path, 'w') as file:
            file.write(response.text)
        print(f"Input downloaded successfully for year {year}, day {day}.")
    else:
        print(f"Failed to download input: HTTP {response.status_code} ({response.reason})")


def main():
    parser = argparse.ArgumentParser(description='Download input for an Advent of Code challenge day.')
    parser.add_argument('--day', type=int, required=True, help='Day of the challenge.')
    parser.add_argument('--year', type=int, default=datetime.now().year, help='Year of the challenge. Defaults to current year.')

    args = parser.parse_args()
    create_structure(args.year, args.day)
    download_input(args.day, args.year)

if __name__ == '__main__':
    main()
