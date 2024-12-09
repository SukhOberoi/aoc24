import itertools
with open(r"day 9\input.txt", "r") as file:
    data = file.read().rstrip("\n")
    checksum = 0
    empty = [int(space) for space in data[1::2]]
    ids = [int(file) for file in data[0::2]]
    new_ids = ids.copy()
    ids = list(enumerate(ids))
    new = [i for sub in itertools.zip_longest(ids, empty) for i in sub]
    del new[-1]
    print(new)
    i = len(new)-1
    
    def merge():
        x=0
        while x< len(new)-1:
            if type(new[x]) == int  and type(new[x+1]) == int:
                new[x] += new.pop(x+1)
                x+=1
            x+=1
    while i>=0:
        if type(new[i]) != int:
            for free in range(len(new)):
                if type(new[free]) == int and new[free] >= new[i][1] and free<i:
                    new[free] -= new[i][1]
                    fit = new.pop(i)
                    new.insert(i, fit[1])
                    new.insert(free, fit)
                    merge()
                    break
        i-=1
    
    
    index = 0
    for x in new:
        if type(x) == int:
            index+=x
        else:
            for i in range(x[1]):
                checksum+=x[0]*index
                index+=1
    print(checksum)
            