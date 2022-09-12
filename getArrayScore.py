#technical tests 2


def getArrayScore(values):
    score = 0
    array_length = values[0]
    array_values = values[1:]
    for index, value in enumerate(values):
        if index % 2 == 0 and value % 2 != 0:
            score += 3
            score -= 2
        elif index % 2 == 0:
            score += 3
        elif value % 2 != 0:
            score -= 2
       
    return score


if __name__ == '__main__':
    values = [4,-21,0,30,-23]
    score = getArrayScore(values)
    print(score)
