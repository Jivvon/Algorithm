import sys

answer = []
tmp_word = []
isReverse = True


def reversed_word(word_list):
    ret = ""
    if word_list:
        word_list.reverse()
        ret = "".join(word_list)
        word_list.clear()
    return ret


for w in sys.stdin.readline().rstrip():
    if w == " ":
        answer.append(reversed_word(tmp_word))
        answer.append(w)
        continue
    elif w == ">":
        isReverse = True
        answer.append(w)
        continue
    elif w == "<":
        isReverse = False
        answer.append(reversed_word(tmp_word))

    if isReverse:
        tmp_word.append(w)
    else:
        answer.append(w)

answer.append(reversed_word(tmp_word))
print("".join(answer))
