with open(r"day 8\input.txt", "r") as file:
    data = file.readlines()
    data = [line.rstrip("\n") for line in data]
    print(data)
    coords = {}
    #get coords of all antennas
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            if char !=".":
                if char not in coords:
                    coords[char] = []
                coords[char].append((y,x))
    print(coords)
    
    #iterate through them and find all mirror images
    ylim = len(data)
    xlim = len(data[0])
    anti = set()
    for type in coords:
        for antenna in coords[type]:
            y,x = antenna
            anti.add((y,x))
            for others in coords[type]:
                if others != antenna:
                    yy, xx = others
                    ydif = yy-y
                    xdif = xx-x
                    newy = y
                    newx = x
                    while True:
                        newy, newx = newy-ydif, newx-xdif
                        if newy>=0 and newy<ylim and newx>=0 and newx<xlim:
                            anti.add((newy,newx))
                        else:
                            break
    print(len(anti))