with open(r"day 15\input.txt", "r") as file:
    data = file.read()
data = [x for x in data.split("\n\n")]
map, moves = data
map = map.split("\n")
moves = list(moves)
while "\n" in moves:
    moves.remove("\n")

walls = set()
boxes = set()
def find_robot():
    for i, row in enumerate(map):
        for j, tile in enumerate(row):
            if tile == "@":
                ans = (i,j)
            if tile == "#":
                walls.add((i,j))
            if tile == "O":
                boxes.add((i,j))
    return ans

robot = find_robot()
def make_move( move):
    global robot
    ry, rx = robot
    my, mx = move
    nexty, nextx = ry+my, rx+mx
    if (nexty, nextx) not in walls and (nexty, nextx) not in boxes:
        robot = (ry+my, rx+mx)
    elif (nexty, nextx) in walls:
        return
    elif (nexty, nextx) in boxes:
        while (nexty, nextx) in boxes:
            nexty += my
            nextx += mx
        if (nexty, nextx) in walls:
            return
        else:
            boxes.add((nexty, nextx))
            boxes.remove((ry+my, rx+mx))
            robot = (ry+my, rx+mx)
        

for move in moves:
    match (move):
        case "^":
            make_move((-1,0))
        case ">":
            make_move((0,1))
        case "v":
            make_move((1,0))
        case "<":
            make_move((0,-1))

gpssum = 0
for box in boxes:
    gpssum += box[0]*100 + box[1]
    
print(gpssum)