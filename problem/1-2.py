import math

def solution(names):
    n = len(set(names))
    m = 4

    numerator = 1;
    denominator = 1;

    for i in range(m):
        numerator *= n - i
        denominator *= (i + 1)
    
    return numerator / denominator

def solution(names):
    n = len(set(names))
    return math.comb(n, 4)
