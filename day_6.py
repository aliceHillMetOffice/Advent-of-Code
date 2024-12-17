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

print(directions[0 % 4])



guard_map = [
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
    finished = False
    i = 0


    while row < len(guard_map) and column < len(guard_map[0]) and not finished:
        direction = directions[i % 4]
        print(direction)
        move_row, move_column = direction_dict.get(direction)
        print(move_row)
        i += 1
        try:
            if guard_map[row][column] == ".":
                mark_x(row, column)
                counter += 1

            if guard_map[row + move_row][column + move_column] == "#":
                break

            if guard_map[row + move_row][column + move_column] is None:
                print("done!")
                finished = True
                return row, column, counter, finished

        except IndexError:
            print("out of range")
            pass

        row += move_row
        column += move_column




    return row, column, counter, finished


start_row, start_column = find_guard_position()


row, column, counter, finished = move_guard(start_row, start_column)
print(counter)




for x in guard_map:
     print(x)
