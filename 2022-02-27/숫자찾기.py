def solution(num, k):
    a = str(num).find(str(k))
    return (a if a == -1 else a+1)
