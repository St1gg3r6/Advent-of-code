with open('aoc_4.txt') as datafile:
    data = [line.rstrip() for line in datafile]

count = 0
xs = 0

for row_number, line in enumerate(data):
    xs += line.count("X")

    for col_number, char in enumerate(line):

        # UP
        if row_number >= 3:
            if char == "X" and data[row_number - 1][col_number] == "M" \
                and data[row_number - 2][col_number] == "A" and data[row_number - 3][col_number] == "S":
                count += 1

        # UP>RIGHT
        if row_number >= 3 and col_number <= len(line) - 4:
            if char == "X" and data[row_number - 1][col_number + 1] == "M" \
                and data[row_number - 2][col_number + 2] == "A" and data[row_number - 3][col_number + 3] == "S":
                count += 1

        # RIGHT
        if col_number <= len(line) - 4:
            if char == "X" and line[col_number + 1] == "M" \
                and line[col_number + 2] == "A" and line[col_number + 3] == "S":
                count += 1

        # DOWN>RIGHT
        if row_number <= len(data) - 4 and col_number <= len(line) - 4:
            if char == "X" and data[row_number + 1][col_number + 1] == "M" \
                and data[row_number + 2][col_number + 2] == "A" and data[row_number + 3][col_number + 3] == "S":
                count += 1

        # DOWN
        if row_number <= len(data) - 4:
            if char == "X" and data[row_number + 1][col_number] == "M" \
                and data[row_number + 2][col_number] == "A" and data[row_number + 3][col_number] == "S":
                count += 1

        # DOWN>LEFT
        if row_number <= len(data) - 4 and col_number >= 3:
            if char == "X" and data[row_number + 1][col_number - 1] == "M" \
                and data[row_number + 2][col_number - 2] == "A" and data[row_number + 3][col_number - 3] == "S":
                count += 1

        # LEFT
        if col_number >= 3:
            if char == "X" and line[col_number - 1] == "M" \
                and line[col_number - 2] == "A" and line[col_number - 3] == "S":
                count += 1

        # UP>LEFT
        if row_number >= 3 and col_number >= 3:
            if char == "X" and data[row_number - 1][col_number - 1] == "M" \
                and data[row_number - 2][col_number - 2] == "A" and data[row_number - 3][col_number - 3] == "S":
                count += 1
        
print(140 * 140, xs, count)
