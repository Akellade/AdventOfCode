from collections import Counter

var = "a"
lower = [(chr(ord(var) + i)) for i in range(26)]
var = "A"
upper = [(chr(ord(var) + i)) for i in range(26)]
paths = []
parttwo = False


def getthing():
    thing = []
    with open("./2021/13/input.txt", "r") as f:
        for line in f.readlines():
            thing.append((line.strip()))
    return thing


def parsething(things):
    coords = []
    folds = []
    for thing in things:
        if thing[0:4] == "fold":
            fold = thing.split(" ")[-1]
            folds.append(fold.split("="))
        elif len(thing) == 0:
            pass
        else:
            coords.append([int(x) for x in thing.split(",")])
    return coords, folds


def plotcoords(coords):
    plot = []
    ymax = 0
    xmax = 0
    coords = sorted(coords)
    for coord in coords:
        if coord[1] > ymax:
            ymax = coord[1]
        if coord[0] > xmax:
            xmax = coord[0]
    line = ["." for i in range(xmax + 1)]
    plot = [line.copy() for i in range(ymax + 1)]

    for coord in coords:
        x, y = coord
        plot[y][x] = "#"

    return plot


def prnt(plot):
    print("")
    for line in plot:
        print(("".join(line)).replace(".", " "))
    print("")


def countdots(plot):
    line = ""
    for p in plot:
        line += "".join(p)
    x = Counter(line)
    print(x["#"])


def doafold(plot, fold):
    dir, val = fold

    if dir == "x":
        for y in range(len(plot) + 1):
            for x in range(int(val), len(plot[-1])):
                diff = int(val) - x
                if plot[y][x] == "#":
                    plot[y][int(val) + diff] = "#"
            for x in reversed(range(int(val), len(plot[-1]))):
                del plot[y][x]
    elif dir == "y":
        for y in range(int(val), len(plot)):
            for x in range(len(plot[-1])):
                diff = int(val) - y
                if plot[y][x] == "#":
                    plot[int(val) + diff][x] = "#"
        for y in reversed(range(int(val), len(plot))):
            del plot[y]


def Solve():
    coords, folds = parsething(getthing())
    plot = plotcoords(coords)

    for fold in folds:

        doafold(plot, fold)
        if fold == folds[0]:
            print("PartOne")
            countdots(plot)

    print("\nPartTwo")
    prnt(plot)


Solve()
