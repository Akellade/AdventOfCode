thing = []

with open("./2022/2/input.txt", "r") as f:
    for line in f.readlines():
        thing.append((line.strip()))

print("Part One")
total = 0
Scores = {"X": 1, "Y": 2, "Z": 3}
WIN = [["A", "Y"], ["B", "Z"], ["C", "X"]]
DRAW = [["A", "X"], ["B", "Y"], ["C", "Z"]]
LOSE = [["A", "Z"], ["B", "X"], ["C", "Y"]]
for line in thing:
    splitline = line.split(" ")
    score = Scores[splitline[1]]
    if splitline in DRAW:
        score += 3
    elif splitline in WIN:
        score += 6
    total += score


# print(thing)
print(total)


print("Part Two")
total = 0
Outcome = {"X": LOSE, "Y": DRAW, "Z": WIN}

for line in thing:
    splitline = line.split(" ")
    outcome = Outcome[splitline[1]]
    for i in outcome:
        if i[0] == splitline[0]:
            score = Scores[i[1]]
            if outcome is DRAW:
                score += 3
            elif outcome is WIN:
                score += 6
            total += score

print(total)
