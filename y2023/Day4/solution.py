# Advent of Code 2023 - Day 4

def calculate_card_value_points(number):
        seed = 1
        for index in range(1, number):
            seed += seed
        return seed


def solve_part1(input_data):
    formatted_data = input_data.strip().split('\n')

    data = [[[int(num) for num in arr.split()]for arr in line.split(":")[1].strip().split(" | ")] for line in formatted_data]
    total=[]
    for card in data:
        res=0
        for num in card[0]:
            if num in card[1]:
                res+=1
        matched_cards=[]
        if res != 0:
            total.append(calculate_card_value_points(res))

    return sum(total)

def calculate_scratchcard_pile(matched_cards_list,scratch_cards_dict):
    for key,value in enumerate(scratch_cards_dict):
        total_per_key = scratch_cards_dict[key]
        range = matched_cards_list[key]

        print(key,value,total_per_key,range)




def solve_part2(input_data):
    formatted_data = input_data.strip().split('\n')
    matched_cards_list = []

    data = [[[int(num) for num in arr.split()]for arr in line.split(":")[1].strip().split(" | ")] for line in formatted_data]
    # scratch_cards_dict = [{i:1} for i in range(1,len(data)+1 )]
    scratch_cards_dict = [1 for i in range(1, len(data) + 1)]
    for card in data:
        res=0
        for num in card[0]:
            if num in card[1]:
                res+=1

        matched_cards_list.append(res)
    print(matched_cards_list)
    calculate_scratchcard_pile(matched_cards_list,scratch_cards_dict)
    # Your solution for Part 2 goes here
    return None
