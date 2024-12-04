import re


def mul(a, b):
    return int(a) * int(b)


def get_data(filename):

    with open(filename) as data_file:
        data = data_file.read()
    return data


def part_one():

    data = get_data('aoc_3.txt')
    matches = re.finditer(r"mul\(\d{1,3},\d{1,3}\)", data, re.MULTILINE)

    total = 0
    for match in matches:
        numbers = re.findall(r"\d{1,3}", match.group())
        total += mul(numbers[0], numbers[1])
    
    return total


def part_two():

    data = get_data('aoc_3.txt')
    matches = re.finditer(r"do(?:n\'t)?\(\)|mul\(\d{1,3},\d{1,3}\)", data, re.MULTILINE)

    total = 0
    calculate = True
    for match in matches:
        if not calculate and match.group() == "do()":
            calculate = True
        if calculate and match.group() == "don't()":
            calculate = False
        if calculate and "mul" in match.group():
            numbers = re.findall(r"\d{1,3}", match.group())
            total += mul(numbers[0], numbers[1])
    
    return total



print(part_one())
print(part_two())