from functools import reduce

size = 140
point_map = [[None for _ in range(size)] for _ in range(size)]

with open("input") as f:
    for i, line in enumerate([line.strip() for line in f.readlines()]):
        for j, char in enumerate(line):
            if char.isdigit():
                char = int(char)
            elif char == ".":
                char = None
            point_map[i][j] = char

# an array of arrays, of which the first value is the number,
# and the second and third values are the starting point and ending points,
# each in the form of a len(2) array with x and y
values = []

start = []
candidate_num_arr = []
for i, row in enumerate(point_map):
    # print(row)
    for j, char in enumerate(row):
        if type(char) is int:
            if len(candidate_num_arr) == 0:
                start = [j, i]
            candidate_num_arr.append(char)
        eol = j == size - 1
        if eol or type(char) is not int:
            if len(candidate_num_arr) > 0:
                candidate_num = 0
                for idx, num in enumerate(reversed(candidate_num_arr)):
                    candidate_num += num * 10 ** idx
                values.append([candidate_num, start, [j - 1, i]])
                candidate_num_arr = []


def get_adjacent_blocks(start, end):
    assert start[1] == end[1]
    baseline_y = start[1]
    result = []
    left_x_bound = start[0] - 1
    right_x_bound = end[0] + 1
    result.append([left_x_bound, baseline_y])
    result.append([right_x_bound, baseline_y])
    result.extend([[x, start[1] - 1] for x in range(left_x_bound, right_x_bound + 1)])
    result.extend([[x, start[1] + 1] for x in range(left_x_bound, right_x_bound + 1)])
    cleaned_result = []
    for it in result:
        if it[0] < 0 or it[0] >= size or it[1] < 0 or it[1] >= size:
            continue
        cleaned_result.append(it)
    # this one-liner doesn't work for some reason
    # [result.remove(it) for it in result if it[0] < 0 or it[0] >= size or it[1] < 0 or it[1] >= size]
    # print(f"{start}, {end}: {cleaned_result}")
    return cleaned_result


valid_values = []
for value, start, end in values:
    gears = list(filter(lambda x: point_map[x[1]][x[0]] is not None and not isinstance(point_map[x[1]][x[0]], int), get_adjacent_blocks(start, end)))
    if (len(gears)) != 0:
        # if a gear matches it only matches one other
        assert len(gears) == 1
        valid_values.append([value, gears[0]])

# print(valid_values)
gear_pairs = []
for it in valid_values:
    matching_gears = list(filter(lambda x: x[1] == it[1], valid_values))
    if len(matching_gears) == 2 and matching_gears not in gear_pairs:
        gear_pairs.append(matching_gears)
print(sum([pair[0][0] * pair[1][0] for pair in gear_pairs]))
# print(sum(valid_values))
# print(map(sum, [value for _ in [list(filter(lambda x: x is not None, get_adjacent_blocks(start, end))) for value, start, end in values] if ]))
