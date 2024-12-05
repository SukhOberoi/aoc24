with open(r"day 5\input.txt", "r") as file:
    data = file.read()
    rules, prints = data.split("\n\n")
    rules = [(int(rule[0:2]),int(rule[3:])) for rule in rules.split("\n")]
    prints = [[int(num) for num in print.split(",")] for print in prints.split()]
    
    

    sum  =0 
    incorrect = []
    for printa in prints:
        flag= True
        for l, r in rules:
            if l in printa and r in printa:
                if not (printa.index(l) < printa.index(r)):
                    flag=False
            if not flag:
                incorrect.append(printa)
                break
        if flag:
            sum+=printa[len(printa)//2]
    
    def order(a,b):
        for l,r in rules:
            if a==l and b==r:
                return 1
            elif a==r and b==l:
                return -1
        return 0
    sum = 0
    
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])

        return merge(left, right)

    def merge(left, right):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if order(left[i] , right[j]) == 1:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result

    sum=0
    for wrong in incorrect:
        fixed = merge_sort(wrong)
        sum += fixed[len(fixed)//2]
    print(sum)
