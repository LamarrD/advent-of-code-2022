def part1(strategy_guide):
    total = 0
    vals = {
        "A X": 1+3, # rock, rock
        "A Y": 2+6, # rock, paper
        "A Z": 3+0, # rock, scissors
        "B X": 1+0, # paper, rock
        "B Y": 2+3, # paper, paper
        "B Z": 3+6, # paper, rock
        "C X": 1+6, # scissors, rock
        "C Y": 2+0, # scissors, paper
        "C Z": 3+3, # scissors, scissors
    }
    for thing in strategy_guide:
        total += vals[thing.strip()]

    return total


def part2():
    total = 0
    vals = {
        "A X": 3+0, # rock, scissors, lose
        "A Y": 1+3, # rock, rock, draw
        "A Z": 2+6, # rock, paper, win
        "B X": 1+0, # paper, rock, lose
        "B Y": 2+3, # paper, paper, draw
        "B Z": 3+6, # paper, scissors, win
        "C X": 2+0, # scissors, paper, lose
        "C Y": 3+3, # scissors, scissors, draw
        "C Z": 1+6, # scissors, rock, win
    }
    for thing in strategy_guide:
        total += vals[thing.strip()]

    return total


if __name__ == "__main__":
    strategy_guide = open("day2/input").readlines()

    print(part1(strategy_guide))
    print(part2())