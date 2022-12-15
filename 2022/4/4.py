import string

thing = []

with open("./2022/4/input.txt", "r") as f:
    for line in f.readlines():
        thing.append((line.strip()))


print("Part One")
total = 0
for sections in thing:
    section1, section2 = sections.split(",")
    s1min, s1max = section1.split("-")
    s2min, s2max = section2.split("-")

    # check 1 in 2 :
    if (int(s1min) >= int(s2min)) and (int(s1max) <= int(s2max)):
        total += 1

    elif (int(s2min) >= int(s1min)) and (int(s2max) <= int(s1max)):
        total += 1


print(total)


# print(thing)


print("Part Two")
total = 0
for sections in thing:
    section1, section2 = sections.split(",")
    s1min, s1max = section1.split("-")
    s2min, s2max = section2.split("-")

    # check 1 in 2 :
    s1range = [i for i in range(int(s1min), int(s1max) + 1)]
    s2range = [i for i in range(int(s2min), int(s2max) + 1)]
    add = 0
    for i in s1range:
        if i in s2range:
            add = 1

    for i in s2range:
        if i in s1range:
            add = 1

    total += add
print(total)
