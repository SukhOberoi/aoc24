def diagonal():
    total = 0
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j]=="M":
                if i+1<len(data) and j+1<len(data[0]) and data[i+1][j+1] == "A":
                    if i+2<len(data) and j+2<len(data[0]) and data[i+2][j+2] == "S":
                        if data[i][j+2] == "M":
                            if data[i+2][j] == "S":
                                total+=1
                        elif data[i][j+2] == "S":
                            if data[i+2][j] == "M":
                                total+=1
            if data[i][j]=="S":
                if i+1<len(data) and j+1<len(data[0]) and data[i+1][j+1] == "A":
                    if i+2<len(data) and j+2<len(data[0]) and data[i+2][j+2] == "M":
                        if data[i][j+2] == "M":
                            if data[i+2][j] == "S":
                                total+=1
                        elif data[i][j+2] == "S":
                            if data[i+2][j] == "M":
                                total+=1
            

                            
    return total

            
        
            
with open(r"day 4\input.txt", "r") as file:
    data = file.readlines()
    data = [line.rstrip("\n") for line in data]
    xmas = diagonal()
    print(xmas)