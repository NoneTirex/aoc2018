data = [line.strip() for line in open("puzzles/day2.txt", 'r')]

def correct_letters(id1, id2):
    if id1.__len__() != id2.__len__():
        return None
    length = id1.__len__()

    found_one_wrong = False
    for i in range(0, length):
        if id1[i] != id2[i]:
            if found_one_wrong:
                return None
            found_one_wrong = True

    if not found_one_wrong:
        return None

    return ''.join([id1[i] for i in range(0, length) if id1[i] == id2[i]])


for i in range(0, data.__len__()):
    for j in range(0, i + 1):
        result = correct_letters(data[i], data[j])
        if result:
            print "Answer: {}".format(result)
