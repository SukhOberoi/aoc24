with open(r"day 12\input.txt", "r") as file:
    data = file.readlines()
    data = [line.rstrip("\n") for line in data]
    

    visited = set()
    def region(coords):
        pericoords = dict()
        area = 1
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
                    rarea, rperi, rpericoords = region((y,x))
                    area += rarea
                    perimeter += rperi
                    for offset in rpericoords:
                        if offset in pericoords:
                            pericoords[offset].extend(rpericoords[offset])
                        else:
                            pericoords[offset] = rpericoords[offset]
            else:
                perimeter += 1
                if offset in pericoords:
                    pericoords[offset].append(coords)
                else:
                    pericoords[offset] = [coords]
        return area, perimeter, pericoords
    
    def merge_horizontal(coords):
        i = 0
        coords = sorted(coords)
        print(coords)
        while i < len(coords) and len(coords) > 1:
            while i+1< len(coords) and coords[i+1][0] == coords[i][0] and coords[i+1][1] == coords[i][1]+1:
                coords.pop(i)
            i+=1
        return len(coords)
    
    def merge_vertical(coords):
        i = 0
        coords = sorted(coords, key=lambda x: (x[1], x[0]))
        print(coords)
        while i < len(coords) and len(coords) > 1:
            while i+1< len(coords) and coords[i+1][1] == coords[i][1] and coords[i+1][0] == coords[i][0]+1:
                coords.pop(i)
            i+=1
        return len(coords)
    
    total = 0
    for i in range(len(data)):
        for j in range(len(data[0])):
            if (i,j) not in visited:
                print(data[i][j])
                area, perimeter, pericoords = region((i,j))
                print(area, perimeter)
                print()
                sides = 0
                for offset in pericoords:
                    if offset == (1,0) or offset == (-1, 0):
                        sides += merge_horizontal(pericoords[offset])
                        print(merge_horizontal(pericoords[offset]))
                    else:
                        sides += merge_vertical(pericoords[offset])
                        print(merge_vertical(pericoords[offset]))
                total+= area*sides
    print(total)

    # _, _, pericoords = region((0,0))
    # print(pericoords)
    # sides = 0
    # for offset in pericoords:
    #     print(offset)
    #     if offset == (1,0) or offset == (-1, 0):
    #         sides += merge_horizontal(pericoords[offset])
    #         print(merge_horizontal(pericoords[offset]))
    #     else:
    #         sides += merge_vertical(pericoords[offset])
    #         print(merge_vertical(pericoords[offset]))
    # print(sides)