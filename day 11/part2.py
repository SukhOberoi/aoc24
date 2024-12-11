from collections import defaultdict
import functools

with open(r"day 11\input.txt", "r") as file:
    data = file.read()
    data = [int(num) for num in data.split()]
    stones = defaultdict(int)
    for stone in data:
        stones[stone]+=1
        
    @functools.cache
    def rule(stone):
        if stone == 0:
            return 1
        elif len(str(stone))%2 == 0:
            num = str(stone)
            num1 = int(num[:len(num)//2])
            num2 = int(num[len(num)//2:])
            return (num1, num2)
        else:
            num = int(stone)*2024
            return num
    
    def blink():
        stonescopy = dict(stones)
        for stone, count in stonescopy.items():
            if count != 0:
                new = rule(stone)
                if type(new) == int:
                    stones[new] += count
                    stones[stone] -=count
                else:
                    num1, num2 = new
                    stones[num1] += count
                    stones[num2] += count
                    stones[stone] -= count
                
    for i in range(75):
        print(i)
        blink()
    print(sum(stones.values()))