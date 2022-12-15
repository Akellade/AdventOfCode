import string

thing = []

with open("./2022/5/input.txt", "r") as f:
    for line in f.readlines():
        thing.append((line))


print("Part One")
MaxStackSize = 0
## setup
for line in thing:
    if "[" in line:
        MaxStackSize += 1
    else:
        break
stacks = []
stacknames = thing[MaxStackSize].split("   ")

for i in stacknames:
    stacks.append([])

for line in thing[MaxStackSize - 1 :: -1]:
    row = line.split(" ")
    for i in range(0, len(stacks)):
        try:
            if line[i * 4 : i * 4 + 4].strip() != "":
                stacks[i].append(line[i * 4 : i * 4 + 4].strip())
        except:
            pass


def move(Num, src, dst):

    for i in range(Num):
        x = stacks[src - 1].pop()
        stacks[dst - 1].append(x)

    ## move complete


for line in thing[MaxStackSize + 2 :]:
    line = line.split(" ")
    move(int(line[1]), int(line[3]), int(line[5]))

output = ""
for stack in stacks:
    output += stack[-1][1]
print(output)

# print(thing)


print("Part Two")
MaxStackSize = 0
## setup
for line in thing:
    if "[" in line:
        MaxStackSize += 1
    else:
        break
stacks = []
stacknames = thing[MaxStackSize].split("   ")

for i in stacknames:
    stacks.append([])

for line in thing[MaxStackSize - 1 :: -1]:
    row = line.split(" ")
    for i in range(0, len(stacks)):
        try:
            if line[i * 4 : i * 4 + 4].strip() != "":
                stacks[i].append(line[i * 4 : i * 4 + 4].strip())
        except:
            pass


def movemany(Num, src, dst):
    x = []
    for i in range(Num):
        x.append(stacks[src - 1].pop())
    for i in range(Num):
        stacks[dst - 1].append(x.pop())
    ## move complete


for line in thing[MaxStackSize + 2 :]:
    line = line.split(" ")
    movemany(int(line[1]), int(line[3]), int(line[5]))

output = ""
for stack in stacks:
    output += stack[-1][1]
print(output)
