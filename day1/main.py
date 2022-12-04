
def part1(elf_calories):
    sum_elf_calories = [sum(elf_calorie) for elf_calorie in elf_calories]
    return max(sum_elf_calories)

def part2(sum_elf_calories):
    sum_elf_calories = [sum(elf_calorie) for elf_calorie in elf_calories]
    first = max(sum_elf_calories)
    sum_elf_calories.remove(first)
    second = max(sum_elf_calories)
    sum_elf_calories.remove(second)
    third = max(sum_elf_calories)
    return first + second + third


if __name__ == "__main__":
    data = open("day1/input").read().split('\n\n')
    elf_calories = [list(map(int, datum.split('\n'))) for datum in data ]
    print(part1(elf_calories))
    print(part2(elf_calories))