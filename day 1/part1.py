with open(r"day 1\input.txt", "r") as file:
    data = file.readlines()
    data = [x.rstrip("\n").split("   ") for x in data]
    data = list(zip(*data))
    list1 = [int(x) for x in sorted(data[0])]
    list2 = [int(x) for x in sorted(data[1])]
    
    total_distance = 0
    for i in range(len(list1)):
        distance = abs(list1[i] - list2[i])
        total_distance += distance
    print(total_distance)