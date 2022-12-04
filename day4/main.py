def part1(data):
    total = 0
    for datum in data:
        ranges = datum.split(',')
        start1,end1 = list(map(int,ranges[0].split('-')))
        start2,end2 = list(map(int,ranges[1].split('-')))

        if start1 <= start2 and end1 >= end2:
            total += 1 
        elif start2 <= start1 and end2 >= end1:
            total += 1
    return total


def part2(data):
    total = 0
    for datum in data:
        ranges = datum.split(',')
        start1,end1 = ranges[0].split('-')
        start2,end2 = ranges[1].split('-')

        range1 = set(range(int(start1),int(end1)+1))
        range2 = set(range(int(start2),int(end2)+1))

        intersection = range1.intersection(range2)
        if len(intersection) > 0:
            total += 1
    return total


if __name__ == "__main__":
    data = open("day4/input").read().splitlines()
    print(part1(data))
    print(part2(data))