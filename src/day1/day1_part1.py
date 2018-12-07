data = [line.strip() for line in open("puzzles/day1.txt", 'r')]

value = sum(map(int, data))

print "Answer: {}".format(value)