"""
day 5
"""

def prepare_rules_list():
    rules_list = []
    with open('day_5_rules.txt', 'r') as file:
        for line in file.readlines():
            line = line.strip().split("|")
            rule = list(map(int, line))
            rules_list.append(rule)
    return rules_list


def prepare_update_list():
    update_list = []
    with open('day_5_updates.txt', 'r') as file:
        for line in file.readlines():
            line = line.strip().split(",")
            update = list(map(int, line))
            update_list.append(update)
    return update_list

test_rules = [[47,53], [97,13], [97,61], [97,47], [75,29], [61,13], [75,53], [29,13], [97,29], [53,29], [61,53], [97,53], [61,29], [47,13], [75,47], [97,75], [47,61], [75,61], [47,29], [75,13], [53,13]]
test_updates = [[75, 47, 61, 53, 29], [97,61,53,29,13], [75,29,13], [75,97,47,61,53], [61,13,29], [97,13,75,29,47]]

RULES_LIST = test_rules
UPDATE_LIST = test_updates

def get_correct_incorrect_lists():
    correct_updates = []
    incorrect_updates = []
    for update in UPDATE_LIST:
        if is_update_in_order(update):
            correct_updates.append(update)
        else:
            incorrect_updates.append(update)
    return correct_updates, incorrect_updates



def is_update_in_order(update) -> bool:
    for rule in RULES_LIST:
        if (rule[0] in update) and (rule[1] in update):
            if update.index(rule[0]) > update.index(rule[1]):
                return False
    return True

def sum_of_middle_numbers(updates):
    middle_numbers = []
    for update in updates:
        middle_num_index = int((len(update) - 1) / 2)
        middle_num = update[middle_num_index]
        middle_numbers.append(middle_num)
    return sum(middle_numbers)

#print(sum_of_middle_numbers(get_correct_incorrect_lists()[0]))


def put_in_order(update):

    for rule in RULES_LIST:
        x, y = rule[0], rule[1]
        if x in update:
            if y in update:
                if update.index(x) > update.index(y):
                    update.pop(update.index(x))
                    update.insert(update.index(y), x)
    return update

print(put_in_order([97,13,75,29,47]))


# if __name__ == "__main__":
    #RULES_LIST = test_rules
    #UPDATE_LIST = test_updates
    # correct, incorrect = get_correct_incorrect_lists()
    # print(incorrect)
    #
    # reordered_updates = put_in_order(incorrect)
    #
    # print(reordered_updates)
    #
    # sum_of_middle_numbers(reordered_updates)
    #
    #
    # print(sum_of_middle_numbers(reordered_updates))


