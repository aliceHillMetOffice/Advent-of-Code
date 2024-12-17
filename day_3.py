"""
advent of code day 3
"""
import re

test_data = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"



day_3_input = []

def get_day_3_input():
    with open("day_3_input.txt") as file:
        for line in file:
            day_3_input.append(line.rstrip())
    return day_3_input


#print(get_day_3_input())

get_day_3_input()
pattern = r"do\(\).*?don't\(\)"

def extract_dos(input):
    data = []
    catch_first_dos = day_3_input[0]
    data += catch_first_dos.split("don't()")
    for element in day_3_input:
        line = re.findall(pattern, element)
        data += line
    return data



def find_muls(dos):
    mul_list = []

    for i in dos:
        muls = re.findall(r'mul\(\d+,\d+\)', i)
        mul_list += muls
    #print(mul_list)
    return mul_list



def counter(input):
    counter = 0
    for i in find_muls(extract_dos(input)):
        #print(i)

        numbers =  re.findall(r'\d+', i)
        numbers = list(map(int, numbers))
        counter += (numbers[0] * numbers[1])
    return counter


print(counter(day_3_input))

print(counter(test_data))









