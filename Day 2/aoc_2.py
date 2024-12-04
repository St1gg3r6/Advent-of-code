import csv


with open('aoc_2.csv') as csv_file:

    csv_reader = csv.reader(csv_file, delimiter=' ')
    data = list(csv_reader)


def part_one():

    safe_reports = 0
    
    for row in data:

        row = [int(value) for value in row]

        ascending = [0 > (row[i] - row[i + 1]) >= -3 for i in range(len(row) - 1)]
        descending = [0 < (row[i] - row[i + 1]) <= 3 for i in range(len(row) - 1)]

        if all(ascending) or all(descending):
            safe_reports += 1

    return safe_reports


def part_two():
    
    safe_reports = 0
    
    for row in data:

        safe = False

        row = [int(value) for value in row]

        for i in range(len(row)):
            test_row = [row[j] for j in range(len(row)) if j != i]
            ascending = [0 > (test_row[j] - test_row[j + 1]) >= -3 for j in range(len(test_row) - 1)]
            if all(ascending):
                safe = True
                break
            descending = [0 < (test_row[j] - test_row[j + 1]) <= 3 for j in range(len(test_row) - 1)]
            if all(descending):
                safe = True
                break

        if safe:
            safe_reports += 1

    return safe_reports


if __name__ == '__main__':
    print(part_one())
    print(part_two())
