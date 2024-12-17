import re

test_wordsearch = [
    "MMMSXXMASM",
    "MSAMXMSMSA",
    "AMXSXMAAMM",
    "MSAMASMSMX",
    "XMASAMXAMM",
    "XXAMMXXAMA",
    "SMSMSASXSS",
    "SAXAMASAAA",
    "MAMMMXMMMM",
    "MXMXAXMASX"
    ]

def prep_wordsearch():
    prepped_wordsearch = []
    with open('day_4_input.txt', 'r') as file:
        for line in file.readlines():
            prepped_wordsearch.append(line.strip())
    return prepped_wordsearch

def count_forward_and_back(wordsearch):
    count_horizontal = sum(len(re.findall('XMAS', s)) for s in wordsearch)
    count_backwards = sum(len(re.findall('SAMX', s)) for s in wordsearch)
    return count_horizontal + count_backwards


def count_vertical_down(wordsearch, x, m, a, s):
    count = 0
    for row in range(len(wordsearch) - 3):
        for column in range(len(wordsearch[row])):
            if (wordsearch[row][column] == x and
                wordsearch[row + 1][column] == m and
                wordsearch[row + 2][column] == a and
                wordsearch[row + 3][column] == s):
                count += 1
    return count

def count_diagonals_down_and_right(wordsearch, x, m, a, s):
    count = 0
    for row in range(len(wordsearch) - 3):
        for column in range(len(wordsearch[row]) - 3):
            if (wordsearch[row][column] == x and
                wordsearch[row + 1][column + 1] == m and
                wordsearch[row + 2][column + 2] == a and
                wordsearch[row + 3][column + 3] == s):
                count += 1
    return count


def count_diagonals_down_and_left(wordsearch, x, m, a, s):
    count = 0
    for row in range(len(wordsearch) - 3):
        for column in range(3, len(wordsearch[row])):
            if (wordsearch[row][column] == x and
                wordsearch[row + 1][column - 1] == m and
                wordsearch[row + 2][column - 2] == a and
                wordsearch[row + 3][column - 3] == s):
                count += 1
    return count


if __name__ == "__main__":
    wordsearch = prep_wordsearch()
    total = count_forward_and_back(wordsearch)
    total += count_diagonals_down_and_right(wordsearch, "X", "M", "A", "S")
    total += count_diagonals_down_and_right(wordsearch, "S", "A", "M", "X")
    total += count_diagonals_down_and_left(wordsearch, "X", "M", "A", "S")
    total += count_diagonals_down_and_left(wordsearch, "S", "A", "M", "X")
    total += count_vertical_down(wordsearch, "X", "M", "A", "S")
    total += count_vertical_down(wordsearch, "S", "A", "M", "X")
    print(total)
