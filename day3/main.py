from itertools import zip_longest


def part1(rucksacks):
    total = 0

    for rucksack in rucksacks:
        half_len = len(rucksack)//2
        firstpart, secondpart = set(rucksack[:half_len]), set(rucksack[half_len:])
        letter = firstpart.intersection(secondpart).pop()
        if letter.isupper():
            total += ord(letter) - 38
        else:
            total += ord(letter) - 96

    return total


def part2(rucksacks):
    total = 0
    grouped_rucksacks = grouper(rucksacks, 3)

    for grouped_rucksack in grouped_rucksacks:
        badge = set(grouped_rucksack[0]).intersection(set(grouped_rucksack[1])).intersection(set(grouped_rucksack[2])).pop()
        if badge.isupper():
            total += ord(badge) - 38
        else:
            total += ord(badge) - 96

    return total


# https://stackoverflow.com/a/434411/11687423
def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)


if __name__ == "__main__":
    rucksacks = open("day3/input").read().splitlines()
    print(part1(rucksacks))
    print(part2(rucksacks))