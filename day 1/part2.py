from collections import Counter


with open(r"day 1\input.txt", "r") as file:
    data = file.readlines()
    data = [x.rstrip("\n").split("   ") for x in data]
    data = list(zip(*data))
    list1 = Counter([int(x) for x in data[0]])
    list2 = Counter([int(x) for x in data[1]])
    similarity_score = 0
    for i in list1:
        similarity_score += i * list1[i] * list2[i]
    print(similarity_score)