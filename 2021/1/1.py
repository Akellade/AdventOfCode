thing = []

with open("./1/input.txt", "r") as f:
    for line in f.readlines():
        thing.append(int(line.strip()))

print("Part One")
last = None
IncCounter = 1  # Off by one error somewhere?
for i in thing:
    if last is None:
        last = i
    else:
        if i > last:
            IncCounter += 1
            last = i
        else:
            last = i

# print(thing)
print(IncCounter)

print("Part Two")
index = 0
IncCounter = 0
i = 0
while True:
    if i + 4 > len(thing):
        break
    a = sum(thing[i : i + 3])

    b = sum(thing[i + 1 : i + 4])

    print("a " + str(a) + " " + str(thing[i : i + 3]))

    print("b " + str(b) + " " + str(thing[i + 1 : i + 4]))
    if b > a:
        IncCounter += 1
    i += 1

print(IncCounter)
