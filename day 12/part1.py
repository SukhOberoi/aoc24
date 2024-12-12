with open(r"day 12\input.txt", "r") as file:
    data = file.readlines()
    data = [line.rstrip("\n") for line in data]
    
    visited = set()
    def region(coords):
        area = 0
        perimeter = 0
        y,x = coords
        visited.add(coords)
        plant = data[y][x]
        offsets = [ (0,1), (1,0), (-1,0), (0, -1)]
        for offset in offsets:
            y,x = coords
            y += offset[0]
            x += offset[1]
            if y>=0 and x>= 0 and y<len(data) and x< len(data[0]) and data[y][x] == plant:
                if ((y,x) not in visited):
                    area+=1
                    rarea, rperi = region((y,x))
                    area += rarea
                    perimeter += rperi
            else:
                perimeter += 1
        return area, perimeter
    total = 0
    for i in range(len(data)):
        for j in range(len(data[0])):
            if (i,j) not in visited:
                print(data[i][j])
                area, perimeter = region((i,j))
                print(area, perimeter)
                print()
                total += (area+1)*perimeter
    print(total)