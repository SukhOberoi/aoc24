with open(r"day 2\input.txt", "r") as file:
    data = file.readlines()
    data = [x.rstrip("\n").split() for x in data]
    data = [[int(x) for x in sublist] for sublist in data]
    safecount = 0 
    for report in data:
        prev = report[0]
        direction = None
        flag = True
        if prev-report[1] < 0:
            direction = "ascending"
        elif prev-report[1] > 0:
            direction = "descending"
        else:
            flag = False
        i = 1
        while i< len(report) and flag == True:
            current = report[i]
            if direction == "ascending":
                if not (current-prev>=1 and current-prev<=3):
                    flag=  False
            elif direction == "descending":
                if not(prev-current>=1 and prev-current<=3):
                    flag = False
            prev= current
            i+=1
        if flag == True:
            safecount +=1
    print(safecount)

