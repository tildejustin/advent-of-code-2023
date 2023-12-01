sum = 0
nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
with open("input") as f:
    for line in f.readlines():
        first = None
        last = None
        linenums = []
        i_to_num = {}

        # preprocess numbers
        for num in nums:
            templine = line
            offset = 0
            while num in templine:
                i_to_num[str(templine.index(num) + offset)] = nums.index(num) + 1
                offset = offset + templine.index(num) + len(num)
                templine = line[offset:]

        for i, c in enumerate(line):
            if c.isnumeric():
                linenums.append(int(c))
            else:
                if i_to_num.get(str(i)) is not None:
                    linenums.append(int(i_to_num.get(str(i))))
        first = int(linenums[0])
        last = int(linenums[-1])
        sum += first * 10 + last
print(sum)
