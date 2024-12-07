from itertools import product
from IPython.display import clear_output
with open(r"day 7\input.txt", "r") as file:
    data = file.readlines()
    data = [line.rstrip("\n") for line in data]
    l = len(data)-1
    ans = 0 
    for i, line in enumerate(data):
        clear_output()
        print(i, "/", l)
        value, nums = line.split(":")
        value = int(value)
        nums = [int(x) for x in nums.split()]
        for opset in product("+*|", repeat = len(nums)-1):
            total = nums[0]
            for i, op in enumerate(opset):
                num1 = total
                num2 = nums[i+1]
                if op == "+":
                    total = num1 + num2
                elif op == "*":
                    total = num1 * num2
                elif op == "|":
                    total = int(str(num1) + str(num2))
            if total == value:
                ans += value
                break
    print(ans)