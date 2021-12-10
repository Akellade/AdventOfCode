thing = []

with open("./3/input.txt", "r") as f:
    for line in f.readlines():
        thing.append((line.strip()))


def getthing():
    thing = []
    with open("./3/input.txt", "r") as f:
        for line in f.readlines():
            thing.append((line.strip()))
    return thing


def getcounter(things, i):
    counter = 0
    for th in things:
        if th[i] == "1":
            counter += 1
    if counter >= len(things) / 2:
        return "1"
    else:
        return "0"


def getcounter2(things, i):
    counter = 0
    for th in things:
        if th[i] == "1":
            counter += 1
    if counter >= len(things) / 2:
        return "0"
    else:
        return "1"


def getepsilon(c):
    epsilon = []
    for bit in c:
        if bit > entries / 2:
            epsilon.append("0")

        else:
            epsilon.append("1")
    epsilon = "".join(gamma)
    return epsilon


entries = len(thing)
bits = len(thing[0])
counters = []
print("Part1")
for i in range(0, bits):
    counters.append(0)
    for line in thing:
        if line[i] == "1":
            counters[i] += 1

gamma = []
epsilon = []
for bit in counters:
    if bit > entries / 2:
        gamma.append("1")
        epsilon.append("0")
    else:
        gamma.append("0")
        epsilon.append("1")

gamma = "".join(gamma)
epsilon = "".join(epsilon)
print(
    "Gamma:{} ({}) * Epsilon:{} ({}) = Power Consumption:{}".format(
        gamma, int(gamma, 2), epsilon, int(epsilon, 2), int(gamma, 2) * int(epsilon, 2)
    )
)
count = 0
print("Part2")

thing = getthing()
oxy = 0
while len(thing) > 1:

    for i in range(0, bits):
        counter = getcounter(thing, i)

        for th in reversed(thing):
            if th[i] != counter:
                thing.remove(th)

oxy = thing[0]
print("OxygenGen = {} ({})".format(oxy, int(oxy, 2)))

thing = getthing()
c02 = 0
while len(thing) > 1:

    for i in range(0, bits):
        if len(thing) == 1:
            break
        counter = getcounter2(thing, i)

        for th in reversed(thing):
            if th[i] != counter:
                thing.remove(th)
c02 = thing[0]
print("C02 scrub = {} ({})".format(c02, int(c02, 2)))

print("result={}".format(int(oxy, 2) * int(c02, 2)))
