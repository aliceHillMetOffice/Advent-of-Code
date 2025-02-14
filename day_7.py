import itertools
import time
start_time = time.time()

# part 1
calibration = {}
with open('day_7_input.txt') as file:
    for line in file:
        x = line.rstrip().split(':')
        result = int(x[0])  # Convert result to integer
        equation = [int(num) for num in x[1].split()]
        calibration[result] = equation


def find_combinations(length, operators):

    combinations = list(itertools.product(operators, repeat=length))
    return combinations


test_data = {190: [10, 19],
3267: [81, 40, 27],
83: [17, 5],
156: [15, 6],
7290: [6, 8, 6, 15],
161011: [16, 10, 13],
192: [17, 8, 14],
21037: [9, 7, 18, 13],
292: [11, 6, 16, 20]}

longest_calibration = (len(max(list(calibration.values()), key=len)))
# #combinations dictionary for speed





def part_1():

    total = 0

    combinations_dict = {}
    for i in range(1, longest_calibration):
        combinations_dict[i] = find_combinations(i, ['*', '+'])

    for result, numbers in calibration.items():


        spaces = len(numbers) - 1
        combinations = combinations_dict[spaces]



        for combination in combinations:
            start = numbers[0]
            for j in range(spaces):
                start = eval(f"{start} {combination[j]} {numbers[j + 1]}")
            test_result = start

            if test_result == result:
                total += result
                break

    return total

#print(part_1())


#part 2



combinations_dict_2 = {}
for i in range(1, longest_calibration):
    combinations_dict_2[i] = find_combinations(i, ['*', '+', '||'])

#print(combinations_dict_2)
cal_list = list(calibration.keys())

def part_2():
    total = 0
    for result, numbers in calibration.items():
        print(cal_list.index(result), "/", len(cal_list))

        spaces = len(numbers) - 1
        combinations = combinations_dict_2[spaces]

        for combination in combinations:
            start = numbers[0]
            for j in range(spaces):
                if combination[j] == '||':
                    start = int(f"{start}{numbers[j + 1]}")
                else:
                    start = eval(f"{start} {combination[j]} {numbers[j + 1]}")
            test_result = start

            if test_result == result:
                total += result
                break

    return total

print(part_2())

total_seconds = (time.time() - start_time)

print("Time taken: ",time.strftime("%H:%M:%S", time.gmtime(total_seconds)))