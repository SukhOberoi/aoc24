with open(r"day 6\input.txt", "r") as file:
    data = file.readlines()
    data = [line.rstrip("\n") for line in data]
    
    def find_guard():
        for i in range(len(data)):
            guard = data[i].find("^")
            if guard != -1:
                data[i] = data[i].replace('^', '.')
                guard = (i, guard)
                return guard
    
    def find_positions(guard):
        visited =  set()
        y, x = guard
        max_d = len(data)
        max_r = len(data[0])
        direction = 'up'
        while y>=0 and y<max_d and x>=0 and x<max_r:
            visited.add((y,x))
            print(y,x, direction)
            if direction == 'up':
                if y-1 == -1 or data[y-1][x] == ".":
                    y = y-1
                else:
                    direction = 'right'
            elif direction == 'right':
                if x+1 == max_r or data[y][x+1] == ".":
                    x +=1
                else:
                    direction = 'down'
            
            elif direction == 'down':
                if y+1 == max_d or data[y+1][x] == ".":
                    y +=1
                else:
                    direction = 'left'
            
            elif direction == 'left':
                if x-1 == -1 or data[y][x-1] == ".":
                    x -=1
                else:
                    direction = 'up'
        return len(visited)
                    
    print(find_positions(find_guard()))
    
    
    