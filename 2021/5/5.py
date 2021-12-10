import os
from datetime import datetime
from collections import Counter
import itertools

def getthing():
    thing = []
    with open("./5/input.txt", "r") as f:
        for line in f.readlines():
            thing.append((line.strip()))
    return thing

def parsething(thing):
    result = []
    for i in thing:
    
        i = i.split(" -> ")
        res = []
        for x in i:
            
            res.append(x.split(","))
        result.append(res)
    return result

def findHorVer(vectors):
    horverresults = []
    diagresults = []
    for v in reversed(vectors):
        if v[0][0]==v[1][0]:
            horverresults.append(v)
        elif v[0][1] == v[1][1]:
            horverresults.append(v)
        else:
            diagresults.append(v)
    return horverresults,diagresults

def genhorvercoords(vectors):
    results = []
    for v in vectors:
        if v[0][0]==v[1][0]:
            rang = sorted((int(v[0][1]), int(v[1][1])))
            # ranges got to be off by one on the end to include the last val! bugger
            for y in range(rang[0],rang[1]+1):
                results.append(((int(v[0][0]),y)))
        if v[0][1]==v[1][1]:
            rang = sorted((int(v[0][0]), int(v[1][0])))
            for x in range(rang[0],rang[1]+1):
                results.append((x,(int(v[0][1]))))
    return results

def gendiagcoords(vectors):
    results = []
    for v in vectors:
        if int(v[0][0]) > int(v[1][0]) :
            xrang = range(int(v[0][0]) , int(v[1][0])-1, -1)
        else:
            xrang = range(int(v[0][0]) , int(v[1][0])+1)

        if int(v[0][1]) > int(v[1][1]) :
            yrang = range(int(v[0][1]) , int(v[1][1])-1,-1)
        else:
             yrang = range(int(v[0][1]) , int(v[1][1])+1)

        xs = [x for x in xrang]
        ys = [y for y in yrang]



        results += list(zip(xs,ys))


    return results


def countcoords(coords):
    coun = Counter(coords)
    result = 0
    for c in coun.keys():
        if coun[c] != 1:
            result +=1
    return result






def PartOne():
    # format thing
    vectors = parsething(getthing())
    # filter for hor or ver
    filteredVectors,trash = findHorVer(vectors)
    # generate all coords
    coords = genhorvercoords(filteredVectors)
    # count coord results
    countedcoords = countcoords(coords)




    print("PartOne")
    print("Number of overlapping points: {}".format(countedcoords))


def PartTwo():
     # format thing
    vectors = parsething(getthing())
    # filter for hor or ver
    filteredVectors,diagvectors = findHorVer(vectors)
    coords = genhorvercoords(filteredVectors)
    coords += gendiagcoords(diagvectors)
    # count coord results
    countedcoords = countcoords(coords)
    print("PartTwo")
    print("Number of overlapping points: {}".format(countedcoords))

            

PartOne()
PartTwo()

            

