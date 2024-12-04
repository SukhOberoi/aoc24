def horizontal():
    total = 0
    for line in data:
        total+= line.count("XMAS") + line.count("SAMX")
    return total

def vertical():
    total = 0
    transpose = [''.join(s) for s in zip(*data)]
    for line in transpose:
        total += line.count("XMAS") + line.count("SAMX")
    return total

def diagonal():
    total = 0
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j]=="X":
                if i+1<len(data) and j+1<len(data[0]) and data[i+1][j+1] == "M":
                    if i+2<len(data) and j+2<len(data[0]) and data[i+2][j+2] == "A":
                        if i+3<len(data) and j+3<len(data[0]) and data[i+3][j+3] == "S":
                            total +=1
                if i+1<len(data) and j-1>=0 and data[i+1][j-1] == "M":
                    if i+2<len(data) and j-2>=0 and data[i+2][j-2] == "A":
                        if i+3<len(data) and j-3>=0 and data[i+3][j-3] == "S":
                            total +=1
            
            elif data[i][j]=="S":
                if i+1<len(data) and j+1<len(data[0]) and data[i+1][j+1] == "A":
                    if i+2<len(data) and j+2<len(data[0]) and data[i+2][j+2] == "M":
                        if i+3<len(data) and j+3<len(data[0]) and data[i+3][j+3] == "X":
                            total +=1
                            
                if i+1<len(data) and j-1>=0 and data[i+1][j-1] == "A":
                    if i+2<len(data) and j-2>=0 and data[i+2][j-2] == "M":
                        if i+3<len(data) and j-3>=0 and data[i+3][j-3] == "X":
                            total +=1
                            
    return total

            
        
            
with open(r"day 4\input.txt", "r") as file:
    data = file.readlines()
    data = [line.rstrip("\n") for line in data]
    ans = horizontal() + vertical() + diagonal()
    print(horizontal() , vertical() , diagonal())
    print(ans)