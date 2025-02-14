

#test = "2333133121414131402" #00...111...2...333.44.5555.6666.777.888899


with open("day_9_input.txt") as file:
    amphipod = file.read().rstrip()


file_block = ""

j = 0

for i in range(len(amphipod)):
    if i % 2 == 0:
        file_block += (str(j) * int(amphipod[i]))
        j += 1
    else:
        file_block += ("." * int(amphipod[i]))

print(file_block) #14 counting from 1




# shuffled_file
shuffled_file = list(file_block)

number_dots = shuffled_file.count(".")
print(number_dots)


print(shuffled_file[-number_dots:] != ".")

i = 0
while "." in shuffled_file:
    if shuffled_file[i] == ".":
        shuffled_file.pop(i)
        lastone = shuffled_file.pop(-1)
        shuffled_file.insert(i, lastone)
    else:
        i += 1




checksum = 0

for k in range(len(shuffled_file)):
    checksum += k * int(shuffled_file[k])

print(checksum)

