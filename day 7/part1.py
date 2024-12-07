from itertools import product
with open(r"day 7\input.txt", "r") as file:
    data = file.readlines()
    data = [line.rstrip("\n") for line in data]
    print(data)
    ans = 0 
    for line in data:
        value, nums = line.split(":")
        value = int(value)
        nums = [int(x) for x in nums.split()]
        print(value, nums)
        for opset in product("+*", repeat = len(nums)-1):
            print(opset)
            total = nums[0]
            for i, op in enumerate(opset):
                num1 = total
                num2 = nums[i+1]
                if op == "+":
                    total = num1 + num2
                elif op == "*":
                    total = num1 * num2
            if total == value:
                ans += value
                break
    print(ans)