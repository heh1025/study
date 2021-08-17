def checkCredit(avg):
    if avg >= 90:
        return "A";
    elif 90 > avg >= 80:
        return "B";
    elif 80 > avg >= 70:
        return "C";
    elif 70 > avg >= 50:
        return "D";
    elif 50 > avg:
        return "F";

#문제 풀이
def solution(scores):
    answer = '';
    avg = [];
 	
    for i in range(0, len(scores)):
        now = [];
        my_score = 0;
        

        for j in range(0, len(scores)):
            now.append(scores[j][i]);
            if j == i:
                my_score = scores[j][i];
        
        if my_score == max(now) or my_score == min(now):
        	
            if now.count(my_score) > 1:
                avg.append(sum(now)/len(now));
            
            else:
                avg.append((sum(now)-my_score)/(len(now)-1));
        
        else:
            avg.append(sum(now)/len(now));
            
    for a in avg:
        answer += checkCredit(a);
        
    
    return answer;