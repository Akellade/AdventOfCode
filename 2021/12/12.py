from os import times_result


var = "a"
lower = [(chr(ord(var) + i)) for i in range(26)]
var = "A"
upper = [(chr(ord(var) + i)) for i in range(26)]
paths = []


def getthing():
    thing = []
    with open("./2021/12/example.txt", "r") as f:
        for line in f.readlines():
            thing.append((line.strip()))
    return thing


def parsething(thing):
    nodes = {}
    for line in thing:
        x, y = line.split("-")
        if x not in nodes.keys():
            nodes[x] = [y]
        else:
            nodes[x].append(y)
        if y not in nodes.keys():
            nodes[y] = [x]
        else:
            nodes[y].append(x)

    nodes = delvaluefromnodes(nodes, "start")
    print(nodes)
    return nodes


def traverse(nodes):
    path = ["start"]
    for node in nodes["start"]:
        thing = path.copy()
        thing.append(node)
        nodes2 = nodes.copy()

        step(thing, nodes2, False)


def delvaluefromnodes(nodes, val):
    for node in nodes.keys():
        if val in nodes[node]:
            nodes[node] = [x for x in nodes[node] if x != val]
    return nodes


def step(path, nodes, caves):
    last = path[-1]

    if last == "end":
        if path not in paths:
            paths.append(path)
            return

    if last[0] in lower and path.count(last) >= 2:
        caves = True

    if last[0] in lower and last != "end" and caves is True:
        # remove the ability to route to it.
        for c in path[1:]:
            if c[0] in lower:
                nodes = delvaluefromnodes(nodes, c)

    if len(nodes[last]) == 0:
        return path

    for node in nodes[last]:
        thing = path.copy()
        thing.append(node)

        nodes2 = nodes.copy()

        step(thing, nodes2, caves)


def PartOne():
    nodes = parsething(getthing())
    traverse(nodes)

    print("PartOne")
    print("found {} paths".format(str(len(paths))))
    for p in paths:
        print(",".join(p))


def PartTwo():

    print("PartTwo")


PartOne()
PartTwo()
