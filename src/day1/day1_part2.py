data = [line.strip() for line in open("puzzles/day1.txt", 'r')]

data = map(int, data)

answers = []
correct_value = False
value = 0

while not correct_value:
    for n in data:
        value += n
        if answers.__contains__(value):
            correct_value = True
            break
        answers.append(value)

print "Answer: {}".format(value)