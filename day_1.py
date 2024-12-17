"""
advent of code day 1:
"""
test_list_1 = [3, 4, 2, 1, 3, 3]
test_list_2 = [4, 3, 5, 3, 9, 3]
list_pairs = []

list_1 = []
list_2 = []

def get_lists():
    """
    reds in location input
    :return:
    """
    with open('day_1_input.txt', 'r') as file:
        for line in file.readlines():
            line = line.split()
            list_1.append(int(line[0]))
            list_2.append(int(line[1]))
    return list_1, list_2


def get_total_difference(list_a, list_b) -> int:
    """
    sort lists, pair values and return total difference
    :param list_a:
    :param list_b:
    :return:
    """
    total_distance = 0
    list_a.sort()
    list_b.sort()
    for i in range(len(list_a)):
        list_pairs.append((list_a[i], list_b[i]))

        total_distance += abs(list_a[i] - list_b[i])
    return total_distance


def get_similarity_score(list_a, list_b):
    scores_list = []
    for i in list_a:
        counter = 0
        for j in list_b:
            if i == j:
                counter += 1
        score = counter * i

        scores_list.append(score)
    return sum(scores_list)





if __name__ == "__main__":
    get_lists()
    #print(get_total_difference(list_1, list_2))
    print(get_similarity_score(test_list_1, test_list_2))
    print(get_similarity_score(list_1, list_2))
