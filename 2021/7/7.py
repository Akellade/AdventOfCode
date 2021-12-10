import os
from datetime import date, datetime
from collections import Counter
import itertools
import timeit


def getthing():
    thing = []
    with open("./7/input.txt", "r") as f:
        for line in f.readlines():
            thing.append((line.strip()))
    return thing


def parsething(thing):
    # list comp to split the string, interpret as ints and return a list of ints.
    result = [int(x) for x in thing[0].split(",")]
    return Counter(result)


def getrange(crabs):
    min = sorted(crabs)[0]
    max = sorted(crabs)[-1]
    return range(min, max + 1)


def solve(crabs, rang):
    lowest = 999999999

    for i in rang:
        result = 0
        for crab in crabs:
            diff = abs(i - crab)
            result += diff * crabs[crab]
        if result < lowest:
            lowest = result
    return lowest


def solve2(crabs, rang):
    lowest = 999999999
    t1 = datetime.now()
    for i in rang:
        result = 0
        for crab in crabs:
            diff = abs(i - crab)
            fuelcost = sum(range(diff + 1))
            result += fuelcost * crabs[crab]
        if result < lowest:
            lowest = result
    print(datetime.now() - t1)
    return lowest


def PartOne():

    print("PartOne")
    crabsubs = parsething(getthing())
    rang = getrange(crabsubs)
    res = solve(crabsubs, rang)
    print("Result = {} ".format(str(res)))


def PartTwo():

    print("PartTwo")
    crabsubs = parsething(getthing())
    rang = getrange(crabsubs)
    res = solve2(crabsubs, rang)
    print("Result = {} ".format(str(res)))


PartOne()
PartTwo()
