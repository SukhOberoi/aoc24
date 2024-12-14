with open(r"day 14\input.txt", "r") as file:
    data = file.readlines()
    data = [x.rstrip('\n') for x in data]
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
    data = robots
    q1, q2, q3, q4 = 0,0,0,0
    seconds = 8000
    width, height  = 101, 103
    # width, height  = 11, 7
    for second in range(seconds):
        print(second)
        mat = [[0 for x in range(width)] for y in range(height)]
        for robot in robots:
            # print(robot)
            vx, vy = robot["vel"]
            dx = vx*second
            dy = vy*second
            px, py = robot["pos"]
            px += dx
            py += dy
            px = px%width
            py = py%height
            mat[py][px] = 1
        
        for row in mat:
            if ''.join(map(str, [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])) in ''.join(map(str, row)):
                for r in mat:
                    print(r)