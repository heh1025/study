def solution(prices):
    answer = [0] * len(prices)

    for i in range(0,len(prices)-1):
        for j in range(i, len(prices)-1):
            if prices[i] >prices[j]:
                break
            else:
                answer[i] +=1
    return answer