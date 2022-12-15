import string

thing = []

with open("./2022/6/input.txt", "r") as f:
    for line in f.readlines():
        thing.append(line.strip())


print("Part One")
for i in range(len(thing[0])):
    window = thing[0][i : i + 4]
    if len("".join(set(window))) == 4:
        print(i + 4)
        break


# print(thing)


print("Part Two")
for i in range(len(thing[0])):
    window = thing[0][i : i + 14]
    if len("".join(set(window))) == 14:
        print(i + 14)
        break
