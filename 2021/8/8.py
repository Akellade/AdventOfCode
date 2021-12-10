import os
from datetime import date, datetime
from collections import Counter
import itertools
import timeit


def getthing():
    thing = []
    with open("./8/input.txt", "r") as f:
        for line in f.readlines():
            thing.append((line.strip()))
    return thing


def parsething(thing):
    signals = []
    chars = []

    for i in thing:
        s = i.split("|")
        signals.append(s[0].split())
        chars.append(s[1].split())
    return signals, chars

def solve1(chars):
    count=0
    for i in chars:
        for c in i:
            if len(c) in (2,3,4,7):
                count+=1
    return count

def solve2(signals,chars):
    results = 0
    for i in range(len(signals)):
        newchars = {}
        while len(newchars)<10:
            for s in signals[i]:
                if len(s) == 2 : 
                    newchars[1] =  "".join(sorted(s))
                elif len(s) == 3:
                    newchars[7] =  "".join(sorted(s))
                elif len(s) == 4:
                    newchars[4] =  "".join(sorted(s))
                elif len(s) == 7:
                    newchars[8] =  "".join(sorted(s))

                elif len(s) == 6:
                    try:
                        thing = "".join(sorted(set(newchars[4]).intersection((sorted(s)))))
                        thing2 = "".join(sorted(s))
                        if "".join(sorted(set(newchars[4]).intersection((sorted(s))))) ==newchars[4] :
                            newchars[9] =  "".join(sorted(s))
                        elif "".join(sorted(set(newchars[1]).intersection((sorted(s))))) ==newchars[1] :
                            newchars[0] =  "".join(sorted(s))
                        else:
                            newchars[6] = "".join(sorted(s))
                    except:
                        pass
                elif len(s) == 5:
                    try:
                        thing= len(sorted(set(newchars[6]).intersection((sorted(s)))))
                        thing2 = "".join(sorted(set(newchars[9]).intersection((sorted(s)))))
                        if "".join(sorted(set(newchars[9]).intersection((sorted(s))))) =="".join(sorted(s)) :
                            
                            if len(sorted(set(newchars[6]).intersection((sorted(s))))) == 5 :
                                newchars[5] =  "".join(sorted(s))
                            else:
                                newchars[3] =  "".join(sorted(s))
                        else:
                            newchars[2] =  "".join(sorted(s))
                    except:
                        pass
        result = []
        for c in chars[i]:
            result.append(str([key for key,item in newchars.items() if item == "".join(sorted(c))][0]))
        results += int("".join(result))
    return results

        
       
 


    




def PartOne():
    signals, chars = parsething(getthing())
    res = solve1(chars)


    print("PartOne")
    print(res)


def PartTwo():
    signals, chars = parsething(getthing())
    res = solve2(signals,chars)
    print("PartTwo")
    print(res)


PartOne()
PartTwo()
