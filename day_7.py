import itertools

calibration = {}
with open("day_7_input.txt") as file:
    for line in file:
        x = line.rstrip().split(":")
        result = int(x[0])  # Convert result to integer
        equation = [int(num) for num in x[1].split()]
        calibration[result] = equation

operator = ["+", "*"]

def find_combinations(spaces):
    combinations = list(itertools.combinations_with_replacement(operator, spaces))
    all_combinations = set()
    for combination in combinations:
        for permutation in list(itertools.permutations(combination, spaces)):
            if permutation not in all_combinations:
                all_combinations.add(permutation)
    return list(all_combinations)


def merge_list(lst1, lst2):
    output = f'{lst1[0]}'
    for i in range(len(lst2)):
        output += f' {lst2[i]} {lst1[i + 1]}'
    return eval(output)


for result, equation in calibration.items():

    spaces = len(equation) - 1
    for combination in find_combinations(spaces):
        trial_result = merge_list(equation, combination)
        if result == trial_result:
            print(result, equation)
            break

