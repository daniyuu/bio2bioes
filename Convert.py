input_file = open("./data/test.txt", "r", encoding="utf-8")

output_file = open("./result/test.txt", "w", encoding="utf-8")


def reformatWordMark(word):
    if (len(word) == 1):
        if word[0][2] != "O":
            word[0] = word[0][0:2] + "S" + word[0][3:]
    else:
        if (len(word[-1]) > 2):
            word[-1] = word[-1][0:2] + "E" + word[-1][3:]
    return word

word = []
text = ""
entity = ""
for line in input_file.readlines():
    if (len(line) > 2):
        text = line[0]
        mark = line[2]

        if mark == "O" or mark == "B" and len(word) != 0:
            word = reformatWordMark(word)
            for newLine in word:
                output_file.write(newLine)
                print(newLine)
            word = []
        word.append(line)

    else:
        # output_file.write(line)
        # print(line)
        word.append(line)
