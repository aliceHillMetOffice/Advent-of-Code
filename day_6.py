"""
day 6

If there is something directly in front of you, turn right 90 degrees.
Otherwise, take a step forward.

"""

direction_dict = {
    "^": (-1, 0),
    ">": (0, 1),
    "v": (1, 0),
    "<": (0, -1)
}

directions = ['^', '>', 'v', '<']



test_guard_map = [
    "....#.....",
    ".........#",
    "..........",
    "..#.......",
    ".......#..",
    "..........",
    ".#..^.....",
    "........#.",
    "#.........",
    "......#..."
]

day_6_input = []

def get_day_6_input():
    with open("day_6_input") as file:
        for line in file:
            day_6_input.append(line.rstrip())
    return day_6_input

get_day_6_input()

guard_map = day_6_input

def find_guard_position():
    for i in range(len(guard_map) - 1):
        if "^" in guard_map[i]:
            starting_row, starting_column = i, guard_map[i].find("^")
            break
    return starting_row, starting_column


def mark_x(row, column):
    try:
        guard_map[row] = guard_map[row][:column] + "X" +  guard_map[row][column + 1:]

    except IndexError:
        pass

    return guard_map


def move_guard(row, column):
    mark_x(row, column)
    counter = 1
    direction_index = 0

    while True:
        direction = directions[direction_index % 4]
        move_row, move_column = direction_dict[direction]

        next_row, next_column = row + move_row, column + move_column

        if not (0 <= next_row < len(guard_map) and 0 <= next_column < len(guard_map[0])):
            break

        if guard_map[next_row][next_column] == "#":
            direction_index += 1
        else:
            row, column = next_row, next_column
            if guard_map[row][column] == ".":
                mark_x(row, column)
                counter += 1

    return counter


start_row, start_column = find_guard_position()[0], find_guard_position()[1]




print(move_guard(start_row, start_column))


for x in guard_map:
     print(x)
