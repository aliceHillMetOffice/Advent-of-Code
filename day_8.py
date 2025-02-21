test_map = [
    "............",
    "........0...",
    ".....0......",
    ".......0....",
    "....0.......",
    "......A.....",
    "............",
    "............",
    "........A...",
    ".........A..",
    "............",
    "............"
]


day_8_input = []

def get_day_8_input():
    with open("day_8_input.txt") as file:
        for line in file:
            day_8_input.append(line.rstrip())
    return day_8_input

real_map = get_day_8_input()


antenna_symbols = set()
for i in test_map:
    antenna_symbols.update(set(i))

antenna_symbols.remove(".")




def find_antennas(antenna_map, character):
    list_0 = []
    node_list = []
    for i in range(len(antenna_map)):
        if character in antenna_map[i]:
            row, column = i, antenna_map[i].find(character)
            list_0.append((row, column))



    length = len(antenna_map) - 1
    width = len(antenna_map[0]) - 1


    
    for antenna in list_0:

        for i in range(len(list_0)):
            if antenna != list_0[i]:
                row_diff = list_0[i][0] - antenna[0]
                column_difference = antenna[1] - list_0[i][1]
                node_1 = (antenna[0] - row_diff, antenna[1] + column_difference)
                node_2 = (list_0[i][0] + row_diff, list_0[i][1] - column_difference)
                if 0 <= node_1[0] <= width and 0 <= node_1[1] <= length:
                    node_list.append(node_1)

                if 0 <= node_2[0] <= width and 0 <= node_2[1] <= length:
                    node_list.append(node_2)



    return set(node_list)




# antinode = set()
#
# for antenna in antenna_symbols:
#     antinode.update(find_antennas(real_map, antenna))
#
# print(len(antinode))



#part 2
#copilot

def parse_map(input_map):
    antenna_positions = {}
    for row in range(len(input_map)):
        for col in range(len(input_map[row])):
            if input_map[row][col] != '.':
                if input_map[row][col] not in antenna_positions:
                    antenna_positions[input_map[row][col]] = []
                antenna_positions[input_map[row][col]].append((row, col))
    return antenna_positions

def calculate_antinode_positions(antenna_positions, map_height, map_width):
    antinodes = set()
    for frequency, positions in antenna_positions.items():
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                row1, col1 = positions[i]
                row2, col2 = positions[j]
                row_diff = row2 - row1
                col_diff = col2 - col1

                # Calculate potential antinode positions
                for k in range(-map_height, map_height):
                    antinode = (row1 + k * row_diff, col1 + k * col_diff)
                    if 0 <= antinode[0] < map_height and 0 <= antinode[1] < map_width:
                        antinodes.add(antinode)

        # Include the positions of the antennas themselves as antinodes
        if len(positions) > 1:
            antinodes.update(positions)
    return antinodes

def count_unique_antinodes(input_map):
    map_height = len(input_map)
    map_width = len(input_map[0])
    antenna_positions = parse_map(input_map)
    antinodes = calculate_antinode_positions(antenna_positions, map_height, map_width)
    return len(antinodes)

# Example usage
input_map = [
    "............",
    "........0...",
    ".....0......",
    ".......0....",
    "....0.......",
    "......A.....",
    "............",
    "............",
    "........A...",
    ".........A..",
    "............",
    "............"
]

print(count_unique_antinodes(real_map))