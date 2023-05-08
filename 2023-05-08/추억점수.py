def solution(name, yearning, photo):
    answer = []
    year_dict = {n:y for n,y in zip(name,yearning)}
    ans = 0
    
    for pho in photo:
        for p in pho:
            if p in year_dict.keys():
                ans += year_dict[p]
        answer.append(ans)
        ans = 0
    
    return answer
