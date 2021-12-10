thing = []

with open("./2/input.txt", "r") as f:
    for line in f.readlines():
        thing.append((line.strip()))


print("Part1")
hor = 0
depth = 0

for th in thing:
    dir, size = th.split(" ")
    if dir == "forward":
        hor += int(size)
    elif dir == "up":
        depth -= int(size)
    elif dir == "down":
        depth += int(size)
    else:
        print("uhoh :" + th)

print("Hor:{} * Depth:{} = {}".format(hor, depth, hor * depth))


print("Part12")
hor = 0
depth = 0
aim = 0

for th in thing:
    dir, size = th.split(" ")
    if dir == "forward":
        hor += int(size)
        depth += aim * int(size)
    elif dir == "up":
        aim -= int(size)
    elif dir == "down":
        aim += int(size)
    else:
        print("uhoh :" + th)

print("Hor:{} * Depth:{} = {}".format(hor, depth, hor * depth))
