with open(r"day 5\input.txt", "r") as file:
    data = file.read()
    rules, prints = data.split("\n\n")
    rules = [(int(rule[0:2]),int(rule[3:])) for rule in rules.split("\n")]
    prints = [[int(num) for num in print.split(",")] for print in prints.split()]
    
    

    sum  =0 
    for printa in prints:
        flag= True
        for l, r in rules:
            if l in printa and r in printa:
                if not (printa.index(l) < printa.index(r)):
                    flag=False
            if not flag:
                break
        if flag:
            sum+=printa[len(printa)//2]
    print(sum)