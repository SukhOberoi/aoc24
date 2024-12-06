import math
with open(r"day 6\input.txt", "r") as file:
    data = file.readlines()
    data = [line.rstrip("\n") for line in data]
    
    def find_guard():
        for i in range(len(data)):
            guard = data[i].find("^")
            if guard != -1:
                guard = (i, guard)
                return guard
    
    def infinite_loop_checker(guard, map):
        # for line in map: print(line)
        # print("--------------------")
        visited = []
        turns = set()
        y, x = guard
        max_d = len(map)
        max_r = len(map[0])
        direction = 'up'
        infinite = False
        while y>=0 and y<max_d and x>=0 and x<max_r:
            if len(visited) == 0 or visited[-1] != (y,x): visited.append((y,x))
            if direction == 'up':
                if y-1 == -1 or map[y-1][x] != "#":
                    y = y-1
                else:
                    direction = 'right'
                    if map[y-1][x]!="^":
                        if (y,x, direction) in turns:
                            infinite = True
                            break;
                        turns.add((y,x, direction))
            elif direction == 'right':
                if x+1 == max_r or map[y][x+1] != "#":
                    x +=1
                else:
                    direction = 'down'
                    if map[y][x+1]!="^":
                        if (y,x, direction) in turns:
                            infinite=True
                            break
                        turns.add((y,x, direction))
            elif direction == 'down':
                if y+1 == max_d or map[y+1][x] != "#":
                    y +=1
                else:
                    direction = 'left'
                    if map[y+1][x]!="^":
                        if (y,x, direction) in turns:
                            infinite=True
                            break
                        turns.add((y,x, direction))
            elif direction == 'left':
                if x-1 == -1 or map[y][x-1] != "#":
                    x -=1
                else:
                    direction = 'up'
                    if map[y][x-1]!="^":
                        if (y,x, direction) in turns:
                            infinite=True
                            break
                        turns.add((y,x, direction))
        return infinite
                    
    option =0
    guard = find_guard()
    for y, i in enumerate(data):
        for x, j in enumerate(i):
            if (y,x) != guard and j != "#":
                map = data.copy()
                map = [list(line) for line in map]
                map[y][x] = "#"
                if infinite_loop_checker(guard, map): option += 1
    print(option)