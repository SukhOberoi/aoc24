import re
enabled = True
def evaluator(hit):
    global enabled
    print(hit)
    if hit=="don't()":
        enabled = False
        return 0
    elif hit== "do()":
        enabled = True
        return 0
    else:
        if enabled:
            hit = hit[4:-1]
            hit = hit.split(",")
            return int(hit[0]) * int(hit[1])
        else:
            return 0

with open(r"day 3\input.txt", "r") as file:
    data = file.read()
    matcher = r"mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don't\(\)"
    hits = re.findall(matcher, data)
    print(hits)
    total = 0
    for hit in hits:
        total += evaluator(hit)
    print(total)