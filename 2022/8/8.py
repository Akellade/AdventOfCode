thing = []

with open("./2022/8/input.txt", "r") as f:
    for line in f.readlines():
        thing.append(line.strip())


print("Part One")
height = len(thing)
width = len(thing[0])
seentrees = []

for y in range(height):
    for x in range(width):
        t = int(thing[y][x])
        if y == 0:
            seentrees.append((x, y))

        elif y == height - 1:
            seentrees.append((x, y))

        elif x == 0:
            seentrees.append((x, y))

        elif x == width - 1:
            seentrees.append((x, y))


for y in range(height):
    highest = 0
    ##Seen from the left

    for x in range(width):
        t = int(thing[y][x])
        if int(thing[y][x]) > highest:
            if (x, y) not in seentrees:
                seentrees.append((x, y))

            highest = int(thing[y][x])

    highest = 0
    ## seen from the right.

    for x in range(width - 1, 0, -1):
        t = int(thing[y][x])
        if int(thing[y][x]) > highest:
            if (x, y) not in seentrees:
                seentrees.append((x, y))

            highest = int(thing[y][x])

for x in range(width):
    highest = 0
    ##Seen from the above
    for y in range(height):
        t = int(thing[y][x])
        if int(thing[y][x]) > highest:
            if (x, y) not in seentrees:
                seentrees.append((x, y))

            highest = int(thing[y][x])
    highest = 0
    ##Seen from the below
    for y in range(height - 1, 0, -1):
        t = int(thing[y][x])
        if int(thing[y][x]) > highest:
            if (x, y) not in seentrees:
                seentrees.append((x, y))

            highest = int(thing[y][x])

print(len(seentrees))
print(len(set(seentrees)))


print("Part Two")
bestscenicscore = 0

for y in range(height):
    for x in range(width):
        tree_c = int(thing[y][x])
        leftC = rightC = upC = downC = 0
        # pick a tree
        # how many left
        coords = [(x2, y) for x2 in range(x - 1, -1, -1)]
        for c in coords:
            a, b = c
            tree_n = int(thing[b][a])

            if tree_n >= tree_c:
                leftC += 1
                # blocked view
                break
            else:
                leftC += 1

        # hor many right
        coords = [(x2, y) for x2 in range(x + 1, width)]
        for c in coords:
            a, b = c
            tree_n = int(thing[b][a])

            if tree_n >= tree_c:
                rightC += 1
                # blocked view
                break
            else:
                rightC += 1
        # how many up
        coords = [(x, y2) for y2 in range(y - 1, -1, -1)]
        for c in coords:
            a, b = c
            tree_n = int(thing[b][a])

            if tree_n >= tree_c:
                # blocked view
                upC += 1
                break
            else:
                upC += 1

        # how many down
        coords = [(x, y2) for y2 in range(y + 1, height)]
        for c in coords:
            a, b = c
            tree_n = int(thing[b][a])

            if tree_n >= tree_c:
                # blocked view
                downC += 1
                break
            else:
                downC += 1

        scenicscore = leftC * rightC * upC * downC

        if scenicscore > bestscenicscore:
            bestscenicscore = scenicscore
            result = "tree = {}, {}, Score  = {}, {}, {}, {}, {}".format(
                tree_c,
                str((x, y)),
                str(scenicscore),
                str(leftC),
                str(rightC),
                str(upC),
                str(downC),
            )

print(result)
