import functools
import re

sum = 0

with open("input") as f:
    for i, game in enumerate(f.readlines()):
        fail = False
        for color, max in (("blue", 14), ("green", 13), ("red", 12)):
            for match in re.findall(f"([0-9]+) {color}", game):
                if int(match) > max:
                    fail = True
                    break
            if fail: break
        if not fail: sum += i + 1

# print(sum)

sum = 0

with open("input") as f:
    for game in f.readlines():
        max = dict()
        for color in ("blue", "green", "red"):
            for match in re.findall(f"([0-9]+) {color}", game):
                if max.get(color) is None or int(match) > max.get(color):
                    max[color] = int(match)
        sum += functools.reduce(lambda a, b: a * b, max.values())

print(sum)
