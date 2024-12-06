import csv
import sys


def get_data(file_name, delimiter):
    with open(file_name) as rules_file:
        return list(csv.reader(rules_file, delimiter=delimiter))


def get_names():
    
    if test:
        rules_file = 'aoc_5_test_rules.csv'
        updates_file = 'aoc_5_test_updates.csv'
    else:
        rules_file = 'aoc_5_rules.csv'
        updates_file = 'aoc_5_updates.csv'
    rules_delimiter = '|'
    updates_delimiter = ','

    return rules_file, rules_delimiter, updates_file, updates_delimiter

def rules_dict(rules):
    rules_dict = {}
    for rule in rules:
        if not rule[0] in rules_dict:
            rules_dict[rule[0]] = [rule[1]]
        else:
            rules_dict[rule[0]].append(rule[1])
    return rules_dict

def sum_middles(arr):
    total = 0
    for item in arr:
        total += int(item[len(item) // 2])
    return total

def main():
    rules_file, rules_delimiter, updates_file, updates_delimiter = get_names()
    rules = rules_dict(get_data(rules_file, rules_delimiter))
    updates = get_data(updates_file, updates_delimiter)
    
    corrects = []
    incorrects = []
    for update in updates:
        is_valid = True
        for i in range(len(update) - 1):
            if update[i] in rules:
                key = update[i]
                for j in range(i + 1, len(update)):
                    if update[j] in rules[key] and is_valid:
                        is_valid = True
                    else:
                        is_valid = False
            else:
                is_valid = False
        if is_valid:
            corrects.append(update)
        else:
            incorrects.append(update)

    total = sum_middles(corrects)

    print(total)

    updates = [item for item in incorrects]
    
    for update in updates:
        is_valid = True
        i = 0
        while i < len(update) - 1:
            if update[i] in rules:
                key = update[i]
                j = i + 1
                while j < len(update):
                    if update[j] in rules[key] and is_valid:
                        is_valid = True
                        j += 1
                    else:
                        temp = update[i]
                        update[i] = update[j]
                        update[j] = temp
                        i -= 1
                        break
                i += 1
            else:
                temp = update[i]
                update[i] = update[i + 1]
                update[i + 1] = temp

    total = sum_middles(updates)
    print(total)

if __name__ == '__main__':
    test = False
    if len(sys.argv) == 2:
        test = True
    main()
