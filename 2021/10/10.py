import os
from datetime import date, datetime
from collections import Counter
import itertools
import timeit
from typing import ByteString


def getthing():
    thing = []
    with open("./10/example.txt", "r") as f:
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
