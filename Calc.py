import math
def stdAbweichung(list):
    mean = sum(list) / len(list)
    var = sum((l - mean) ** 2 for l in list) / len(list)
    return math.sqrt(var)