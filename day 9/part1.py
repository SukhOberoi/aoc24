with open(r"day 9\input.txt", "r") as file:
    data = file.read().rstrip("\n")
    print(data)
    checksum = 0
    empty = [int(space) for space in data[1::2]]
    print(empty)
    ids = [int(file) for file in data[0::2]]
    print(ids)
    index = 0
    for i in range(len(ids)):
        val = ids[i]
        for x in range(index, index+val):
            checksum += i * x
            # print(i , "*", x)
            index+=1
            ids[i]-=1
        if i<len(empty):
            for x in range(index, index+empty[i]):
                last = len(ids)-1
                while ids[last] == 0 and last != 0: last-=1
                checksum += last * x
                # print(last , "*", x)
                ids[last] -= 1
                index+=1
    print(checksum)
            