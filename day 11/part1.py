with open(r"day 11\input.txt", "r") as file:
    data = file.read()
    data = [int(num) for num in data.split()]
    print(data)

    def blink():
        index = 0 
        while index< len(data):
            stone = data[index]
            if stone == 0:
                data[index] = 1
            elif len(str(stone))%2 == 0:
                num = str(stone)
                num1 = int(num[:len(num)//2])
                num2 = int(num[len(num)//2:])
                data[index] = num1
                data.insert(index+1, num2)
                index+=1
            else:
                num = stone*2024
                data[index] = num
            index+=1
                
    for i in range(25):
        blink()
    print(len(data))