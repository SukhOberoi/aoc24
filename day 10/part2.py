def find_trails(coords, tile):
    nines = 0
    y, x= coords
    if y>=0 and x>=0 and y<len(data) and x <len(data[0]) and data[y][x] == tile:
        if tile == "9":
            nines+=1
            return nines
        new_tile = chr(ord(tile)+1)
        nines+=(find_trails((y+1, x), new_tile))
        nines+=(find_trails((y-1, x), new_tile))
        nines+=(find_trails((y, x+1), new_tile))
        nines+=(find_trails((y, x-1), new_tile))
        return nines
    else:
        return 0

with open(r"day 10\input.txt", "r") as file:
    data = file.readlines()
    data = [line.rstrip("\n") for line in data]
    total = 0
    for y, row in enumerate(data):
        for x, tile in enumerate(row):
            if tile == "0":
                nines = find_trails((y,x), "0")
                total += (nines)
    print(total)