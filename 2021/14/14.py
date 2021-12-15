from collections import Counter
from itertools import pairwise
from time import perf_counter

var = "a"
lower = [(chr(ord(var) + i)) for i in range(26)]
var = "A"
upper = [(chr(ord(var) + i)) for i in range(26)]
paths = []
parttwo = False


def getthing():
    thing = []
    with open("./2021/14/input.txt", "r") as f:
        for line in f.readlines():
            thing.append((line.strip()))
    return thing


def parsething(things):
    rules = {i.split(" -> ")[0]: i.split(" -> ")[1] for i in things[2:]}
    starter = things[0]

    return rules, starter


def tick(rules, starter):
    start = perf_counter()
    outputstring = "a"

    windows = [
        "{}{}".format(starter[i], starter[i + 1]) for i in range(len(starter) - 1)
    ]
    for w in windows:

        outputstring = outputstring[:-1] + rules[w]
    print(
        "{} taken to process {} insertions".format(
            perf_counter() - start, str(len(outputstring) - len(starter))
        )
    )
    return outputstring


def processrules(rules):
    for key, val in rules.items():

        string = "{}{}{}".format(key[0], val, key[1])
        rules[key] = string

    return rules


def PartOne():
    print("PartOne")

    rules, starter = parsething(getthing())

    processrules(rules)

    TurnCounter = 40
    for i in range(TurnCounter):
        starter = tick(rules, starter)

    startercounter = Counter(starter)
    thing = startercounter.most_common()[-1]
    diff = startercounter.most_common(1)[0][1] - startercounter.most_common()[-1][1]
    print(
        "{} - {} = {}".format(
            startercounter.most_common(1), startercounter.most_common()[-1], diff
        )
    )


PartOne()
