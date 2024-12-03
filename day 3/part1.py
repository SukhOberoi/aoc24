import re
def evaluator(hit):
    hit = hit[4:-1]
    hit = hit.split(",")
    return int(hit[0]) * int(hit[1])

with open(r"day 3\input.txt", "r") as file:
    data = file.read()
    matcher = r"mul\([0-9]{1,3},[0-9]{1,3}\)"
    hits = re.findall(matcher, data)
    total = 0
    for hit in hits:
        total += evaluator(hit)
    print(total)