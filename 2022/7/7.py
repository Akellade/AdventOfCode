thing = []

with open("./2022/7/input.txt", "r") as f:
    for line in f.readlines():
        thing.append(line.strip())


def command(input):
    input = input.split(" ")
    global directory

    if input[1] == "cd":
        if input[2] == "/":
            directory = "/"
            tree[directory] = 0

        elif input[2] == "..":
            directory = directory.split("/")[:-2]
            directory = "/".join(directory) + "/"
        else:
            directory += input[2] + "/"


def addDir(input):
    input = input.split(" ")
    if directory + input[1] + "/" not in tree.keys():
        tree[(directory + input[1]) + "/"] = 0


def addFileSize(input):
    input = input.split(" ")
    tree[directory] += int(input[0])


tree = {}

print("Part One")
for hist in thing:
    if "$" in hist:
        command(hist)
    elif "dir" in hist:
        addDir(hist)
    else:
        addFileSize(hist)

        # Add node to current level


# print(thing)
total = 0


for key in tree.keys():
    branchTotalSize = [tree[i] for i in tree.keys() if key in i]
    if sum(branchTotalSize) <= 100000:
        total += sum(branchTotalSize)
print(total)

print("Part Two")

totalUsedfilesystemsize = sum([tree[i] for i in tree.keys() if "/" in i])
totalFileSystemSize = 70000000
targetFreeSpace = 30000000
free = totalFileSystemSize - totalUsedfilesystemsize
candidates = []
for key in tree.keys():
    branchTotalSize = [tree[i] for i in tree.keys() if key in i]
    if sum(branchTotalSize) >= targetFreeSpace - free:
        candidates.append(sum(branchTotalSize))
print(min(candidates))
