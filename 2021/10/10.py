import os
from datetime import date, datetime
from collections import Counter
import itertools
import timeit
from typing import ByteString


chars = {"(":")","[":"]","{":"}","<":">"}
scores = {")":3,"]":57,"}":1197,">":25137}
scores2 = {"(":1,"[":2,"{":3,"<":4}
opens = ['(','[','{','<']
ends= [')',']','}','>']

def getthing():
    thing = []
    with open("./2021/10/input.txt", "r") as f:
        for line in f.readlines():
            thing.append((line.strip()))
    return thing


def solve1(thing):
    total  = 0
    for line in thing:
        checker = []
        for c in line:
            if c in opens:
                checker.append(c)
            elif c in ends and chars[checker[-1]] ==c:
                checker.pop()
            else:
                total+= scores[c]

                break
    return total

def solve2(thing):
    scores = []
    
    for line in thing:
        error=False
        total  = 0
        checker = []
        for c in line:
            
            if c in opens:
                checker.append(c)
            elif c in ends and chars[checker[-1]] ==c:
                checker.pop()
            else:
                error=True
                break
        if not error and len(checker):
            for c in reversed(checker):
                total*=5
                total += scores2[c]
            scores.append(total)
    return sorted(scores)

def PartOne():
    
    res = solve1(getthing())

    print("PartOne")
    print(res)


def PartTwo():

    print("PartTwo")
    res = solve2(getthing())
    print(res[int(len(res)/2)])


PartOne()
PartTwo()
