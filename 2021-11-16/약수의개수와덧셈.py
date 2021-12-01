def solution(left, right): 
    answer = 0 
    for num in range(left, right + 1): 
        operator = 1 
        divisor_num = len([n for n in range(1, num+1) if num % n == 0]) 
        
        if divisor_num % 2 == 1: 
                operator = -1 
        answer += num * operator 
    return answer