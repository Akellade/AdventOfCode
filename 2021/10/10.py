import os
from datetime import date, datetime
from collections import Counter
import itertools
import timeit
from typing import ByteString


chars = {"(":")","[":"]","{":"}","<":">"}
scores = {")":3,"]":57,"}":1197,">":25137}

def getthing():
    thing = []
    with open("./2021/10/example.txt", "r") as f:
        for line in f.readlines():
            thing.append((line.strip()))
    return thing


def filterIncomplete(thing):
    output=[]
    for line in thing:
        if isLineComplete(line):
            output.append(line)
    return output


def isLineComplete(line):
    if len(line) % 2 ==0:
        return True
    else:
        return False

def isOpening(string):
    if string in ['(','[','{','<']:
        return True
def isClosing(string):
    if string in [')',']','}','>']:
        return True

def findClosing(line,open=''):
    # {()()()>
    chars = {"(":")","[":"]","{":"}","<":">"}

    if open=='':
        if isOpening(line[0]):
            x = findClosing(line[1:],line[0])
            return x
        elif isClosing(line[0]):
            return scores[line[0]]
    elif isOpening(line[0]):
        x =  findClosing(line[1:],line[0])
        return x
    elif isClosing(line[0]):
        if chars[open] == line[0]:
            x= isClosing(line[1:])
        else:
            return scores[line[0]]
    




def solve1(thing):
    total =0
    for l in thing:
        total +=findClosing(l)
    return total
    


def PartOne():
    thing = filterIncomplete(getthing())
    res = solve1(thing)

    print("PartOne")
    print(res)


def PartTwo():

    print("PartTwo")


PartOne()
PartTwo()
