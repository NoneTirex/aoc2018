data = [line.strip() for line in open("puzzles/day1_input1.txt", 'r')]

value = 0

for n in data:
    value += int(n)

print(value)