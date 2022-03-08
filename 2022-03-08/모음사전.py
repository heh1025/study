def solution(word):
    char = {'A': 0, 'E': 1, 'I': 2, 'O': 3, 'U': 4}
    answer = len(word)
    re = (((5 + 1) * 5 + 1) * 5 + 1) * 5 + 1 
    for i in word:
        answer += re * char[i]
        re = (re - 1) // 5
    return answer
