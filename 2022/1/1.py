thing = []

with open("./2022/1/input.txt", "r") as f:
    for line in f.readlines():
        thing.append((line.strip()))

print("Part One")
elves = []
elf = 0
total = 0
for line in thing:
    try:
        total += int(line)
    except:
        elves.append(total)
        total = 0
        elf += 1


# print(thing)
print(
    "Number of elves:{}\nlargest calorie count:{}".format(elf + 1, max(elves))
)


print("Part Two")
thing2 = sorted(elves, reverse=True)
total = thing2[0] + thing2[1] + thing2[2]
print(total)
