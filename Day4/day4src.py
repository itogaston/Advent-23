import re
from functools import reduce
import numpy as np

def get_numbers(line: str) -> (list, list):
    halfs = line.split("|")

    winners_str = halfs[0].split(":")[1].strip()
    winners = str_to_list(winners_str)

    my_numbers_str = halfs[1].strip()
    my_numbers = str_to_list(my_numbers_str)

    return winners, my_numbers

def get_winners(winners: list, numbers: list) -> int:
    winners_set = set(winners)
    numbers_set = set(numbers)

    intersection = numbers_set.intersection(winners_set)

    return len(intersection)

def str_to_list(numbers_str: str) -> list:
    numbers = numbers_str.replace("  ", " ").split(" ")
    numbers = list(map(lambda x: int(x), numbers))
    return numbers

def first(filename):
    # Open the file and read its content.
    with open(filename) as f:
        content = f.readlines()

    # Start the count
    count = 0

    for line in (content):
        winners, numbers = get_numbers(line)
        n = get_winners(winners, numbers)

        if (n>0):
            count += 2**(n-1)

    return count

def second(filename):
    # Open the file and read its content.
    with open(filename) as f:
        content = f.readlines()

    # Start the count
    count = 0

    length = len(content)

    cards = np.ones(length)

    for index, line in enumerate(content):
        winners, numbers = get_numbers(line)
        n_winners = get_winners(winners, numbers)
        n = np.zeros(length)
        n[index+1:index+1+n_winners] += 1
        cards += cards[index] * n

    return np.sum(cards, dtype= int)

if __name__ == "__main__":
    filename = "input"
    
    count = first(filename)
    print(f"first: {count}")
    if filename == "test_input":
        assert count == 13

    count = second(filename)
    print(f"second: {count}")
    if filename == "test_input":
        assert count == 30