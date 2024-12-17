"""
advent of code day 2:
"""

example_data = [[7, 6, 4, 2, 1], [1, 2, 7, 8, 9], [9, 7, 6, 2, 1], [1, 3, 2, 4, 5], [8, 6, 4, 4, 1], [1, 3, 6, 7, 9]]

example_2 = [[38, 41, 44, 47, 50, 47], [75, 78, 79, 82, 85, 85], [11, 13, 16, 19, 21, 25], [39, 40, 43, 44, 50], [75, 77, 80, 78, 80, 83, 84, 87]]

def prep_data():
    data = []

    with open('day_2_input.txt', 'r') as file:
        for line in file.readlines():
            line = line.strip().split(" ")
            report = list(map(int, line))
            data.append(report)

    return data

def calculate_number_of_safe_reports(data):
    #loop through report
    number_of_safe_reports = 0

    for report in data:
        if safe_logic(report):
            number_of_safe_reports += 1
        elif problem_damper(report):
            number_of_safe_reports += 1
    return number_of_safe_reports

def safe_logic(report: list):
    """
    The levels are either all increasing or all decreasing.
    Any two adjacent levels differ by at least one and at most three.
    :return: True if the report is safe, otherwise False
    """
    differences_list = [report[i + 1] - report[i] for i in range(len(report) - 1)]

    if all(1 <= abs(diff) <= 3 for diff in differences_list) and (
            all(diff > 0 for diff in differences_list) or all(diff < 0 for diff in differences_list)):
        return True
    return False


def problem_damper(report: list) -> bool:
    """
    Checks if removing a single level from an unsafe report makes it safe.
    :return: True if the report is safe after removing one level, otherwise False
    """
    for i in range(len(report)):
        new_report = report[:i] + report[i+1:]
        if safe_logic(new_report):
            return True

    return False


if __name__ == "__main__":
    #print(problem_damper([1, 3, 2, 4, 5]))
    print(calculate_number_of_safe_reports(prep_data()))
    #print(calculate_number_of_safe_reports(example_data))
