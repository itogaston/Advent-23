import numpy as np

def first(filename):
    # Open the file and read its content.
    with open(filename) as f:
        content = f.readlines()

    # Start the count
    count = 0

    for line in (content):

        game = create_game(line)

        if check_game(game):
            count += game["gameId"]
        
    return count

def create_game(rounds: list[str]) -> dict:
    game = {}

    words = rounds.split()

    gameID = int(words[1].replace(":", ""))

    game["gameId"] = gameID

    game_rounds = rounds.split(";")
    game_rounds[0] = game_rounds[0].split(":")[1]

    game["rounds"] = []
    # print(rounds)
    for index, round in enumerate(game_rounds):
        
        round = round.strip()
        round = round.split()

        roundInfo = {}
        for i in range(1, len(round), 2):
            roundInfo[round[i].replace(",", "")] = int(round[i-1])
        
        game["rounds"].append(roundInfo)
    # print(game["rounds"])
    return game

def check_game(game: dict[str, int]) -> bool:
    constraints = {"red": 12, "green": 13, "blue": 14}

    rounds = game["rounds"]

    for round in rounds:
        for color, ammount in round.items():
            if color in constraints.keys() and ammount > constraints[color]:
                return False
            elif color not in constraints.keys():
                return False

    return True

def second(filename):
    # Open the file and read its content.
    with open(filename) as f:
        content = f.readlines()

    # Start the count
    count = 0

    for line in (content):

        game = create_game(line)

        minimum_config = get_minimum(game)

        count += np.prod(list(minimum_config.values()))

        
    return count

def get_minimum(game: dict) -> dict:
    rounds = game["rounds"]
    minimum = {"red": 0, "green": 0, "blue": 0}

    for round in rounds:
        for color, ammount in round.items():
            if (ammount > minimum[color]):
                minimum[color] = ammount
    
    return minimum

if __name__ == "__main__":
    filename = "input"
    
    count = first(filename)
    print(count)
    if filename == "test_input":
        assert count == 8

    count = second(filename)
    print(count)
    if filename == "test_input":
        assert count == 2286