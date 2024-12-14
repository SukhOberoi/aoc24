with open(r"day 14\input.txt", "r") as file:
    data = file.readlines()
    data = [x.rstrip('\n') for x in data]
    print(data)
    robots = []
    for robot in data:
        px = int(robot[robot.find("=")+1: robot.find(",")])
        py = int(robot[robot.find(',')+1: robot.find(' ')])
        vx = int(robot[robot.find('=', robot.find(' '))+1: robot.find(',', robot.find(' '))])
        vy = int(robot[robot.find(',', robot.find(' '))+1:])
        robots.append({
            "pos" : (px, py),
            "vel" : (vx, vy)
        })
    q1, q2, q3, q4 = 0,0,0,0
    seconds = 100
    width, height  = 101, 103
    # width, height  = 11, 7
    for robot in robots:
        print(robot)
        vx, vy = robot["vel"]
        dx = vx*seconds
        dy = vy*seconds
        px, py = robot["pos"]
        px += dx
        py += dy
        px = px%width
        py = py%height
        robot['pos'] = (px, py)
        x, y = '', ''
        if px < width//2:
            x = 'left'
        elif px> width//2:
            x = 'right'
        
        if py < height//2:
            y = 'up'
        elif py> height//2:
            y = 'down'
        robot['quadrant'] = 0
        if x and y and x == 'left' and y == 'up':
            robot['quadrant']= 1
            q1+=1
        elif x and y and x == 'right' and y == 'up':
            robot['quadrant']= 2
            q2+=1
        elif x and y and x == 'left' and y == 'down':
            robot['quadrant']= 3
            q3+=1
        elif x and y and x == 'right' and y == 'down':
            robot['quadrant']= 4
            q4+=1
        print(robot)
        print()
    
    print(q1*q2*q3*q4)
    print(q1,q2,q3,q4)