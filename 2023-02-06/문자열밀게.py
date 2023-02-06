def solution(A, B):
    answer = 0
    text = list(A)
    for i in range(len(A)):
        if "".join(text) == B:
            return answer
        else:
            text.insert(0, text.pop())
            answer += 1
            
    return -1
