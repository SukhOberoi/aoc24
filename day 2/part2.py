with open(r"day 2\input.txt", "r") as file:
    data = file.readlines()
    data = [x.rstrip("\n").split() for x in data]
    data = [[int(x) for x in sublist] for sublist in data]
    safecount = 0 
    def isSafe(report):
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
        return flag

    for report in data:
        if isSafe(report):
            safecount+=1
        else:
            for i in range(len(report)):
                if isSafe([*report[:i], *report[i+1:]]):
                    safecount+=1
                    break
    print(safecount)

