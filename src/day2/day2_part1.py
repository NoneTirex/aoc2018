data = [line.strip() for line in open("puzzles/day2.txt", 'r')]

result = {2: 0, 3: 0}

for text in data:
    in_line = {2: False, 3: False}
    for n in text:
        count = text.count(n)
        if count == 2 and not in_line[2]:
            result[2] += 1
            in_line[2] = True
        elif count == 3 and not in_line[3]:
            result[3] += 1
            in_line[3] = True

print "Answer: {}".format(result[2] * result[3])