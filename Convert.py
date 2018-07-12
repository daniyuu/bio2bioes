file_name = "validation.txt"

input_file = open("./data/{0}".format(file_name), "r", encoding="utf-8")
output_file = open("./result/{0}".format(file_name), "w", encoding="utf-8")


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
index = 0
for line in input_file.readlines():
    print(index)
    index += 1
    if (len(line) > 2):
        text = line[0]
        mark = line[2]

        if mark == "O" or mark == "B":
            if len(word) != 0:
                word = reformatWordMark(word)
                for newLine in word:
                    output_file.write(newLine)
                word = []
        word.append(line)

    else:
        word.append(line)
