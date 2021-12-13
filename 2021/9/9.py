from collections import Counter


def getthing():
    thing = []
    with open("./2021/9/input.txt", "r") as f:
        for line in f.readlines():
            thing.append((line.strip()))
    return thing


def parsething(thing):
    return thing


def parsething2(thing):
    for x in range(len(thing)):
        thing[x] = [i for i in thing[x]]
    return thing


def solve1(thing):
    total = 0
    testedvalcount = 0
    lowpoints = []
    for y in range(len(thing)):
        for x in range(len(thing[0])):
            testcoords = [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]
            if y == 0:
                testcoords.remove((x, y - 1))
            elif y == len(thing) - 1:
                testcoords.remove((x, y + 1))
            if x == 0:
                testcoords.remove((x - 1, y))
            elif x == len(thing[0]) - 1:
                testcoords.remove((x + 1, y))
            if isLowPoint(int(thing[y][x]), testcoords, thing):
                total += int(thing[y][x]) + 1
            testedvalcount += 1
    return total


def isLowPoint(val, testcoords, thing):

    # logstring = "Value :{} ".format(val)

    for coord in testcoords:
        # logstring+= "{} {} ".format(coord, thing[coord[1]][coord[0]])
        # print(int(thing[coord[1]][coord[0]]))
        if int(thing[coord[1]][coord[0]]) <= val:
            # logstring+="Failed"
            # print(logstring)
            return False
    # logstring += "Success"
    # print(logstring)
    return True


def solve2(thing):
    # Replace vals with unique unicode char to identify basins
    # iterate a few times to ensure no stragglers
    # when iterating swap range to iterate in reverse

    var = "®"
    chars = [(chr(ord(var) + i)) for i in range(2048)]
    nums = [str(x) for x in range(0, 9)]
    basincount = 0
    lastresult = []

    yrange = range(len(thing))
    xrange = range(len(thing[0]))

    rang = (yrange, xrange)
    revrang = (reversed(yrange), reversed(xrange))

    itercount = 0
    curval = ""
    while itercount < 10:
        if itercount % 2 == 0:
            ran = rang
        else:
            ran = revrang
        for y in ran[0]:
            for x in ran[1]:
                if thing[y][x] == "9":
                    pass
                else:
                    curval = thing[y][x]
                    testcoords = [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]
                    if y == 0:
                        testcoords.remove((x, y - 1))
                    elif y == len(thing) - 1:
                        testcoords.remove((x, y + 1))
                    if x == 0:
                        testcoords.remove((x - 1, y))
                    elif x == len(thing[0]) - 1:
                        testcoords.remove((x + 1, y))
                    newval = chars[basincount]
                    todocoords = []
                    possiblevals = []
                    for coord in testcoords:

                        if thing[coord[1]][coord[0]] in chars:
                            if thing[coord[1]][coord[0]] not in possiblevals:
                                possiblevals.append(thing[coord[1]][coord[0]])
                                newval = "zz"
                                todocoords.append(coord)
                        elif thing[coord[1]][coord[0]] in nums:
                            todocoords.append(coord)

                    if newval == chars[basincount]:
                        thing[y][x] = chars[basincount]
                        for c in todocoords:
                            thing[c[1]][c[0]] = chars[basincount]
                        basincount += 1
                    else:
                        if len(possiblevals) == 1:
                            thing[y][x] = possiblevals[0]
                            newval = possiblevals[0]
                        else:
                            out = ""
                            for i in thing:
                                out += "".join(i)

                            x = Counter(out)
                            wincharcount = 0

                            for p in possiblevals:
                                if x[p] > wincharcount:
                                    wincharcount = x[p]
                                    newval = p
                        for c in todocoords:
                            thing[c[1]][c[0]] = newval

        out = ""
        for i in thing:
            out += "".join(i)
            print("".join(i).replace("9", " "))
        out = out.replace("9", "")
        x = Counter(out).most_common(3)
        itercount += 1
        lastresult = x
        print(x)

    return x[0][1] * x[1][1] * x[2][1]


def PartOne():
    thing = parsething(getthing())
    res = solve1(thing)

    print("PartOne")
    print(res)


def PartTwo():

    print("PartTwo")
    thing = parsething2(getthing())
    res = solve2(thing)
    print(res)


PartOne()
PartTwo()
