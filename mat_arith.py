# There is no need to import SAMPLE_MATRICES
# YOUR CODE AND HEADING HERE


def mat_sum(m1, m2):
    if len(m1) == len(m2) and len(m1[0]) == len(m2[0]):
        newList = [[0 for x in range(len(m1[0]))] for y in range(len(m1))]
        for m, y in enumerate(m1):
            for n, x in enumerate(y):
                newList[m][n] = x + m2[m][n] 
    
        return newList

    return "no solution"


def mat_mul(m1, m2):
    if len(m1[0]) == len(m2):
        newList = [[0 for x in range(len(m2[0]))] for y in range(len(m1))]

        for m in range(len(m1)):
            for n in range(len(m2[0])):
                newList[m][n] = sum([i * m2[count][n] for count, i in enumerate(m1[m])])

        return newList

    return "no solution"