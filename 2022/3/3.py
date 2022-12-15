import string

thing = []

with open("./2022/3/input.txt", "r") as f:
    for line in f.readlines():
        thing.append((line.strip()))


print("Part One")
oddchars = ""
total = 0

for bag in thing:
    bag1, bag2 = bag[: len(bag) // 2], bag[len(bag) // 2 :]

    for i in bag1:
        if i in bag2:
            oddchars += i
            break


for o in oddchars:
    char = ord(o)
    if o in string.ascii_uppercase:
        char -= 64
        char += 26
    else:
        char -= 96
    total += char

print(total)


# print(thing)


print("Part Two")

x = [i for i in range(0, len(thing), 3)]
oddchars2 = ""
total = 0
for i in x:
    group = thing[i : i + 3]
    for ch in group[0]:
        if ch in group[1]:
            if ch in group[2]:
                oddchars2 += ch
                break
for o in oddchars2:
    char = ord(o)
    if o in string.ascii_uppercase:
        char -= 64
        char += 26
    else:
        char -= 96
    total += char
print(total)
