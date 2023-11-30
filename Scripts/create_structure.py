import argparse
import datetime
import sys
import os


def main(day, year):
    if year is None:
        year = datetime.date.today().year

    year_dir = f"../{str(year)}"
    if not os.path.exists(year_dir):
        os.makedirs(year_dir)

    if day is None:
        print("Day not specified.")
        sys.exit(1)

    day_dir = os.path.join(year_dir, f"Day{day}")
    if not os.path.exists(day_dir):
        os.makedirs(day_dir)

        # Create puzzle.py and input.txt
        with open(os.path.join(day_dir, "puzzle.py"), 'w') as f:
            f.write("# Advent of Code\n# Year {}, Day {}\n".format(year, day))

        with open(os.path.join(day_dir, "input.txt"), 'w') as f:
            pass

    else:
        print(f"The directory {day_dir} already exists.")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Parse Day and Year for AdventOfCode coding challenge")
    parser.add_argument('--day', help="Day of challenge", type=int)
    parser.add_argument('--year', help="Year of challenge", type=int)
    args = parser.parse_args()
    sys.exit(main(args.day, args.year))
