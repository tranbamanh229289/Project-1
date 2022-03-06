import random
from ..constant import N_ARTICLE

def AND(posting1, posting2):
    p1 = 0
    p2 = 0
    result = list()
    len_posting1= len(posting1)
    len_posting2 = len(posting2)
    while p1<len_posting1 and p2<len_posting2:
        if posting1[p1] == posting2[p2]:
            result.append(posting1[p1])
            p1 += 1
            p2 += 1
        elif posting1[p1] > posting2[p2]:
            p2 += 1
        else:
            p1 += 1
    return result

def OR(posting1, posting2):
    p1 = 0
    p2 = 0
    result = list()
    len_posting1 = len(posting1)
    len_posting2 = len(posting2)
    while p1 < len_posting1 and p2 < len_posting2:
        if posting1[p1] == posting2[p2]:
            result.append(posting1[p1])
            p1 += 1
            p2 += 1
        elif posting1[p1] > posting2[p2]:
            result.append(posting2[p2])
            p2 += 1
        else:
            result.append(posting1[p1])
            p1 += 1
    while p1 < len(posting1):
        result.append(posting1[p1])
        p1 += 1
    while p2 < len(posting2):
        result.append(posting2[p2])
        p2 += 1
    return result
# NOT is going to return indexes of documents that are not included in the given posting list.
def NOT(posting):
    result = list()
    i = 0
    for item in posting:
        while i < item:
            result.append(i)
            i += 1
        else:
            i += 1
    else:
        while i < N_ARTICLE:
            result.append(i)
            i += 1
    return result
