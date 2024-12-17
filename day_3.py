"""
advent of code day 3
"""
import re

#test_data = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

pattern = r"do\(\).*?don't\(\)"

def extract_dos():

    with open('day_3_input.txt', 'r') as file:
        data = []
        for line in file.readlines():
            #print(line)
            line = re.findall(pattern, line)
            data += line


    return data



def find_muls():
    mul_list = []

    for i in extract_dos():
        muls = re.findall(r'mul\(\d+,\d+\)', i)
        mul_list += muls
    print(mul_list)
    return mul_list



def counter():
    counter = 0
    for i in find_muls():
        print(i)

        numbers =  re.findall(r'\d+', i)
        numbers = list(map(int, numbers))
        counter += (numbers[0] * numbers[1])
    return counter


print(counter())








