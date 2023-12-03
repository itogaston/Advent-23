import re
from functools import reduce

def get_numbers_and_symbols_v2(line):
    line_aux = re.sub(r"(\W)", r".\1.", line)
    items = line_aux.replace(".", " ").split()
    
    numbers = []
    symbols = []
    start_at = 0
    for item in items:
        # 123
        if item.isnumeric():
            match = re.search(item, line[start_at:].replace(".", " "))
            numbers.append((item, match.start()+start_at, match.end()+start_at))
            start_at = match.end()+start_at
        # *
        else:
            match = re.search(rf"\{item}", line[start_at:].replace(".", " "))
            symbols.append((item, match.start()+start_at, match.end()+start_at))
            start_at = match.end()+start_at

    return numbers, symbols
    
def get_numbers_and_symbols(line):
    items = line.replace(".", " ").split()

    numbers = []
    symbols = []

    for item in items:
        # 123
        if item.isnumeric():
            match = re.search(item, line.replace(".", " "))
            numbers.append((item, match.start(), match.end()))
        # *
        elif len(item) == 1:
            match = re.search(rf"\{item}", line.replace(".", " "))
            symbols.append((item, match.start(), match.end()))
        # 617* 
        else:
            print(item)
            if item[0].isnumeric():
                match = re.search(item[0:-1], line.replace(".", " "))
                numbers.append((item[0:-1], match.start(), match.end()))

                match = re.search(rf"\{item[-1]}", line.replace(".", " "))
                symbols.append((item[-1], match.start(), match.end()))
            else:
                match = re.search(item[1:], line.replace(".", " "))
                numbers.append((item[1:], match.start(), match.end()))   
            
                match = re.search(rf"\{item[0]}", line.replace(".", " "))
                symbols.append((item[0], match.start(), match.end()))


    return numbers, symbols
    
def get_adjents_numbers(number_matrix: list[list], symbol_matrix: list[list]) -> list:
    correct_numbers = []
    for index, numbers in enumerate(number_matrix):
        symbols = symbol_matrix[max(0, index-1):index+2]
        for number in numbers:
            possible_symbols = [item for symbol_aux in symbols for item in symbol_aux]
            symbol = list(filter(lambda x: x[1] >= number[1]-1 and x[1] <= number[2], possible_symbols))
            if(len(symbol) > 0):
                correct_numbers.append(number)
    return correct_numbers

def get_adjents_numbers_star(number_matrix: list[list], symbol_matrix: list[list]) -> list:
    correct_numbers = []
    for index, symbols in enumerate(symbol_matrix):
        numbers = number_matrix[max(0, index-1):index+2]
        for symbol in symbols:
            possible_numbers = [item for number_aux in numbers for item in number_aux]
            adjent_numbers = list(filter(lambda x: symbol[1] >= x[1]-1 and symbol[1] <= x[2], possible_numbers))
            if(len(adjent_numbers) > 1):
                correct_numbers.append(adjent_numbers)
    return correct_numbers


def first(filename):
    # Open the file and read its content.
    with open(filename) as f:
        content = f.readlines()

    # Start the count
    count = 0
    
    numbers = []
    symbols = []

    for line in (content):
        numbers_aux, symbols_aux = get_numbers_and_symbols_v2(line)
        numbers.append(numbers_aux)
        symbols.append(symbols_aux)

    numbers_adjents = get_adjents_numbers(numbers, symbols)

    numbers_adjents = list(map(lambda x: int(x[0]), numbers_adjents))
    count = reduce(lambda x, y: x+y, numbers_adjents)
    return count

def second(filename):
    # Open the file and read its content.
    with open(filename) as f:
        content = f.readlines()

    # Start the count
    count = 0
    
    numbers = []
    symbols = []

    for line in (content):
        numbers_aux, symbols_aux = get_numbers_and_symbols_v2(line)
        numbers.append(numbers_aux)
        symbols.append(symbols_aux)

    # list of list of tuples
    numbers_adjents = get_adjents_numbers_star(numbers, symbols)
    
    # first get ratio
    ratios = []
    for ratio in numbers_adjents:
        ratios.append(reduce(lambda x, y: int(x[0]) * int(y[0]), ratio))
    
    count = reduce(lambda x, y: x+y, ratios)
    return count

if __name__ == "__main__":
    filename = "input"
    
    count = first(filename)
    print(f"first: {count}")
    if filename == "test_input":
        assert count == 4361

    count = second(filename)
    print(f"second: {count}")
    if filename == "test_input":
        assert count == 467835