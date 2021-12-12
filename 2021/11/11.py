def getthing():
    thing = []
    with open("./2021/11/example.txt", "r") as f:
        for line in f.readlines():
            thing.append((line.strip()))
    return thing

def parsething(thing):
    for x in range(len(thing)):
        thing[x] = [i for i in thing[x]]
    return thing

def getTestCoords(x,y,thing):
    testcoords = [
        (x, y + 1),
        (x, y - 1),
        (x + 1, y),
        (x - 1, y),
        (x + 1, y + 1),
        (x - 1, y - 1),
        (x + 1, y - 1),
        (x - 1, y + 1),
    ]

    for i in reversed(range(len(testcoords))):
        if testcoords[i][0] ==10 or testcoords[i][1] == 10:
            del testcoords[i]
        elif testcoords[i][0] == -1 or testcoords[i][1] ==-1:
            del testcoords[i]

    return testcoords

def tick(thing):
    flashcount =0
    flashvals = []
    for y in range(len(thing)):
        for x in range(len(thing[0])):
            if thing[y][x] == '9':
                thing[y][x] = 'a'
                flashvals.append( (x,y))

            elif thing[y][x] == 'a':
                pass
            else:
                thing[y][x] = str(int(thing[y][x]) + 1)
    
    if len(flashvals )==1:
        for x,y in flashvals:
            testcoords = getTestCoords(x,y,thing)
            thing = flash(thing,testcoords)
    elif len(flashvals )>1:
        for f in flashvals:
            x=f[0]
            y=f[1]
            testcoords = getTestCoords(x,y,thing)
            thing = flash(thing,testcoords)
    
    for y in range(len(thing)):
        for x in range(len(thing[0])):
            if thing[y][x] == 'a':
                thing[y][x] = '0'
                flashcount+=1
    return thing,flashcount

def flash(thing,coords):
    flashvals = []
    for x,y in coords:

        if thing[y][x] == '9':
            flashvals.append((x,y))
            thing[y][x] = 'a'
        elif thing[y][x] == 'a':
            pass
        else : 
            thing[y][x] = str(int(thing[y][x]) + 1)
    
    if len(flashvals )==1:
        for x,y in flashvals:
                testcoords = getTestCoords(x,y,thing)
                thing = flash(thing,testcoords)
    elif len(flashvals )>1:
        testcoords = getTestCoords(x,y,thing)
        thing = flash(thing,testcoords)
    return thing



def solve1(thing):
    stepcount = 100
    total = 0
    for i in range(stepcount):
        print("iteration: {} ".format(i))
        for t in thing:
            print(t)
        thing,flashcount = tick(thing)
        total += flashcount

    return total


def PartOne():
    thing = parsething(getthing())
    res = solve1(thing)

    print("PartOne")
    print(res)


def PartTwo():

    print("PartTwo")



PartOne()
PartTwo()
