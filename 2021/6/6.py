from datetime import datetime
from collections import Counter


def getthing():
    thing = []
    with open("./2021/6/input.txt", "r") as f:
        for line in f.readlines():
            thing.append((line.strip()))
    return thing


def parsething2(thing):
    # list comp to split the string, interpret as ints and return a list of ints.
    result = [int(x) for x in thing[0].split(",")]
    return Counter(result)


def parsething(thing):
    # list comp to split the string, interpret as ints and return a list of ints.
    result = [int(x) for x in thing[0].split(",")]
    return result


def tick1(fish):
    newfish = 0

    for i in range(len(fish)):
        if fish[i] == 0:
            fish[i] = 6
            newfish += 1
        else:
            fish[i] -= 1

    for i in range(newfish):
        fish.append(8)
    return fish


def tick2(fish):
    newfish = 0

    for key in range(0, 9):

        if key == 0 and fish[key] > 0:
            fish[7] += fish[0]
            newfish += fish[0]
            fish[0] = 0
        else:
            fish[key - 1] = fish[key]
            fish[key] = 0
    fish = addfish(newfish, fish)
    return fish


def addfish(count, fish):
    fish[8] += count

    # for i in range(count):
    #     fish.append(8)
    return fish


def simulate(fish, days):
    t1 = datetime.now()
    for i in range(days):
        fish = tick1(fish)
    print(datetime.now() - t1)
    return fish


def simulate2(fish, days):
    t1 = datetime.now()
    for i in range(days):
        fish = tick2(fish)
    print(datetime.now() - t1)
    return fish


def PartOne():
    print("PartOne")
    fish = parsething(getthing())
    simfish = simulate(fish, 80)

    print(len(simfish))


def PartTwo():

    print("PartTwo")
    fish = parsething2(getthing())
    simfish = simulate2(fish, 256)
    print(sum(simfish.values()))


PartOne()
PartTwo()
