with open('aoc_4.txt') as datafile:
    data = [line.rstrip() for line in datafile]

count = 0

for row_number in range(1, len(data) - 1):

    for col_number in range(1, len(data[0]) - 1):

        char = data[row_number][col_number]

        if char == "A":
            # DOWN>RIGHT AND UP>RIGHT
            if data[row_number - 1][col_number - 1] == "M" \
                and data[row_number + 1][col_number - 1] == "M" \
                and data[row_number - 1][col_number + 1] == "S" \
                and data[row_number + 1][col_number + 1] == "S":
                count += 1

            # DOWN>RIGHT AND DOWN>LEFT
            if data[row_number - 1][col_number - 1] == "M" \
                and data[row_number - 1][col_number + 1] == "M" \
                and data[row_number + 1][col_number + 1] == "S" \
                and data[row_number + 1][col_number - 1] == "S":
                count += 1

            # UP>LEFT AND DOWN>LEFT
            if data[row_number + 1][col_number + 1] == "M" \
                and data[row_number - 1][col_number + 1] == "M" \
                and data[row_number - 1][col_number - 1] == "S" \
                and data[row_number + 1][col_number - 1] == "S":
                count += 1

            # UP>LEFT AND UP>RIGHT
            if data[row_number + 1][col_number + 1] == "M" \
                and data[row_number + 1][col_number - 1] == "M" \
                and data[row_number - 1][col_number - 1] == "S" \
                and data[row_number - 1][col_number + 1] == "S":
                count += 1

        
print(140 * 140, count)
