import numpy as np
from tqdm import tqdm
import re

def first(filename):
    # Open the file and read its content.
    with open(filename) as f:
        content = f.readlines()

    # Start the count
    count = 0

    for line in tqdm(content):
        digit_mask = np.array([char.isdigit() for char in line])
        chars = np.array([char for char in line])
        digits = chars[digit_mask]
        count += np.int32(digits[0]+digits[-1])

    print(count)
    return count

def second(filename):
    values = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    
    # Open the file and read its content.
    with open(filename) as f:
        content = f.readlines()

    # Start the count
        count = 0

    for line in (content):
        line_digitalized = line
        for token, digit in values.items():
            # replace word two by string "t"+"2"+"o" (token[0]+digit+token[-1])
            line_digitalized = line_digitalized.replace(token, token[0]+digit+token[-1])
        digit_mask = np.array([char.isdigit() for char in line_digitalized])
        chars = np.array([char for char in line_digitalized])
        digits = chars[digit_mask]
        count += int(digits[0]+digits[-1])

    print(count)
    return count

if __name__ == "__main__":
    filename = "input"
    first(filename)
    second(filename)